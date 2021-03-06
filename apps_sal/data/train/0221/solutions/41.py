class Solution:

    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        low = 0
        high = n - 1
        nums = [ord(S[i]) - ord('a') for i in range(n)]

        def findDuplicate(L):
            h = 0
            a = 26
            modulus = 2 ** 32
            for i in range(L):
                h = (h * a + nums[i]) % modulus
            seen = {h}
            aL = pow(a, L, modulus)
            for start in range(1, n - L + 1):
                h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
                if h in seen:
                    return start
                seen.add(h)
            return -1
        res = ''
        while low < high:
            mid = (low + high + 1) // 2
            start = findDuplicate(mid)
            if start != -1:
                low = mid
                res = S[start:start + mid]
            else:
                high = mid - 1
        return res
