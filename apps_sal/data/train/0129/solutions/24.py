class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # A = [8 , 1 ,5 ,2 6,]
        # output = 11
        # Explanation:
        # i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
        i = A[0]
        max_ans = 0
        for j in range(1, len(A)):
            x = A[j]
            print(x)
            max_ans = max(max_ans, i + x - j)
            i = max(i, x + j)
        return max_ans
