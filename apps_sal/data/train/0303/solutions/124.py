class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [[0 for _ in range(len(A))] for _ in range(2)]

        dp2 = [0 for _ in range(len(A))]

        for i in range(len(A)):

            startIndex = max(0, i - K + 1)
            currMax = 0
            while startIndex <= i:
                currMax = max(currMax, A[startIndex])
                if startIndex - 1 >= 0:
                    dp2[i] = max(dp2[startIndex - 1] + max(A[startIndex:i + 1]) * (i + 1 - startIndex), dp2[i])
                else:
                    dp2[i] = max(A[:i + 1]) * (i + 1)

                startIndex += 1

        print(dp2)
        return dp2[-1]
