class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [0] * len(B)
        d = {}
        for i in range(len(B)):
            b = B[i]
            if b in d:
                d[b].append(i)
            else:
                d[b] = [i]
        for a in A:
            if a in d:
                for k in d[a][::-1]:
                    if k == 0:
                        dp[k] = 1
                    else:
                        dp[k] = dp[k - 1] + 1
                    for i in range(k + 1, len(dp)):
                        if dp[i] < dp[i - 1]:
                            dp[i] = dp[i - 1]
                        else:
                            break
                    # print(dp)
        return max(dp)
