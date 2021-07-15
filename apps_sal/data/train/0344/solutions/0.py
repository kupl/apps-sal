class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        dp = [(1, 1)] * len(A[0])
        for i in range(len(dp)):
            if i > 0:
                max_pre = None
                for pre in range(i - 1, -1, -1):
                    for word in A:
                        if word[pre] > word[i]:
                            pre -= 1
                            break
                    else:
                        if max_pre is None or dp[pre][1] > dp[max_pre][1]:
                            max_pre = pre

                max_len = 1 if max_pre is None else max(1, dp[max_pre][1] + 1)
                overall = max(dp[i - 1][0], max_len)
                dp[i] = (overall, max_len)
        # print(dp)
        return len(dp) - dp[-1][0]
