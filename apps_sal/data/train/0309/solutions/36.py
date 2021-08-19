class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0

        dp = []
        for _ in range(len(A)):
            dp.append(dict())
        dp[0][0] = 1

        for i in range(1, len(A)):
            dp[i][0] = 1
            for j in range(i):
                # continue subsequence
                diff = A[i] - A[j]
                if diff in dp[j]:
                    if diff not in dp[i]:
                        dp[i][diff] = dp[j][diff] + 1
                    else:
                        dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)

                # start new subsequence
                else:
                    dp[i][diff] = 2

        # for x in dp:
        #     print(str(x))
        return max([max(x.values()) for x in dp])
