class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [{} for i in range(n)]
        result = 2

        for i in range(1, n):
            for j in range(i):
                delta = A[i] - A[j]

                if delta in dp[j]:
                    currentLength = dp[j].get(delta)
                    dp[i][delta] = currentLength + 1

                else:
                    dp[i][delta] = 2

                result = max(result, dp[i][delta])
        return result

    def longestArithSeqLength2(self, A: List[int]) -> int:
        from collections import Counter
        cnt = Counter()
        cnt
        arith = [Counter() for i in range(len(A))]
        longest = 0
        for i in range(len(A) - 2, -1, -1):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                arith[i][diff] = max(1 + arith[j][diff], arith[i][diff])
                longest = max(longest, arith[i][diff])

        return longest + 1
