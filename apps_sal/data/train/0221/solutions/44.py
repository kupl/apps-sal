class Solution:
    def longestDupSubstring(self, S):
        nums = [ord(c) - ord('a') for c in S]
        BASE, MOD = 26, 2**32               # Wrong: BASE, MOD = 113, 1000000007, too small

        def check(L):
            cur_hash, seen = 0, set()
            for val in nums[:L]:
                cur_hash = ((cur_hash * BASE) + val) % MOD
            seen.add(cur_hash)
            X = pow(BASE, L - 1, MOD)         # much faster than (BASE ** (L-1)) % MOD
            for i, val in enumerate(nums[L:]):
                # cur_hash -= nums[i] * (BASE ** (L-1))
                cur_hash -= nums[i] * X
                cur_hash = ((cur_hash * BASE) + val) % MOD
                if cur_hash in seen:
                    return i + 1
                seen.add(cur_hash)
            return -1
        low, high = 1, len(S) + 1
        res = 0
        while low < high:
            mid = (low + high) // 2
            idx = check(mid)
            if idx != -1:
                low = mid + 1
                res = idx
            else:
                high = mid
        return S[res: res + low - 1]
