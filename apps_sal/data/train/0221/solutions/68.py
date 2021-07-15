class Solution:
    def longestDupSubstring(self, S: str) -> str:
        def search(m, MOD):
            h = 0
            for i in range(m):
                h = (h * 26 + nums[i]) % MOD
            s = {h}
            aL = pow(26, m, MOD)
            for pos in range(1, n - m + 1):
                h = (h * 26 - nums[pos - 1] * aL + nums[pos + m - 1]) % MOD
                if h in s:
                    return pos
                s.add(h)
            return -1
        
        n = len(S)
        nums = [ord(c) - ord('a') for c in S]
        # find length of longest duplicate substring
        l, r = 1, n
        pos = 0
        MOD = 2**63 - 1 # use largest positive of 8 byte integer
        while l <= r:
            m = (l + r) // 2
            # search if there's duplicate for length m substring
            cur = search(m, MOD)
            if cur != -1:
                l = m + 1
                pos = cur
            else:
                r = m - 1
        return S[pos: pos + l - 1]
