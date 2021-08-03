class Solution:
    def longestDupSubstring(self, S):
        nums, N = [ord(c) - ord('a') for c in S], len(S)
        BASE, MOD = 26, 2**32

        def check(L):
            cur_hash, seen = 0, set()
            for val in nums[:L]:
                cur_hash = (cur_hash * BASE + val) % MOD
            seen.add(cur_hash)
            X = pow(BASE, L - 1, MOD)
            for idx, val in enumerate(nums[L:]):
                cur_hash -= nums[idx] * X
                cur_hash = (cur_hash * BASE + val) % MOD
                if cur_hash in seen:
                    return idx + 1
                seen.add(cur_hash)
            return -1
        low, high = 1, N + 1
        start = 0
        while low < high:
            mid = (low + high) // 2
            idx = check(mid)
            if idx != -1:
                low = mid + 1
                start = idx
            else:
                high = mid
        return S[start: start + low - 1]
