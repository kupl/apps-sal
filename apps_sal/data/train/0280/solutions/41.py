class Solution:

    def palindromePartition(self, s: str, k: int) -> int:
        sLen = len(s)
        dp = {}

        def moveOnce(prei, i0, k0):
            if (prei, i0, k0) in dp:
                return dp[prei, i0, k0]
            if k0 == k:
                l = prei
                r = sLen - 1
                subAns = 0
                while r > l:
                    if s[r] != s[l]:
                        subAns += 1
                    r -= 1
                    l += 1
                dp[prei, i0, k0] = subAns
                return subAns
            l = prei
            r = i0
            subAns = 0
            while r > l:
                if s[r] != s[l]:
                    subAns += 1
                r -= 1
                l += 1
            if sLen - i0 - 1 <= k - k0:
                return subAns
            subAns = min(subAns + moveOnce(i0 + 1, i0 + 1, k0 + 1), moveOnce(prei, i0 + 1, k0))
            dp[prei, i0, k0] = subAns
            return subAns
        return moveOnce(0, 0, 1)
