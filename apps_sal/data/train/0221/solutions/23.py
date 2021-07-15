class Solution:
    def longestDupSubstring(self, S: str) -> str:
        N = len(S)
        l, r = 1, N
        nums = [ord(x) - ord('a') for x in S]
        KMAX = 2 ** 63 - 1
        def check(m):
            MAXL = pow(26, m, KMAX)
            total, hashset = 0, set()
            for i in range(m):
                total = (total * 26 + nums[i]) % KMAX
            hashset.add(total)
            for i in range(1, N - m + 1):
                total = (total * 26 - MAXL * nums[i-1] + nums[i+m-1]) % KMAX
                if total in hashset:
                    return i
                hashset.add(total)
            return -1
        
        while l < r:
            m = (l + r) // 2
            if check(m) < 0:
                r = m
            else:
                l = m + 1
        idx = check(r - 1)        
        return S[idx: idx + r-1]
