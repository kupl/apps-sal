class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def _len(cnt): return 1 if cnt == 1 else 1 + len(str(cnt))
        dp = [[0]*(k+1) for _ in range(len(s)+1)]

        for ki in range(k+1):
            for left in range(ki, len(s)):
                drop = dp[left-1][ki-1] if ki > 0 else float('inf')
                keep = 1 + dp[left-1][ki]
                cnt = 1
                kj = ki
                for j in range(left-1, -1, -1):
                    if s[j] != s[left]:
                        if kj == 0:
                            break
                        kj -= 1
                    else:
                        cnt += 1
                        keep = min(keep, _len(cnt) + dp[j-1][kj])

                dp[left][ki] = min(keep, drop)

        return dp[len(s)-1][k]

