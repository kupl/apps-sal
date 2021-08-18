class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        i = A[0]
        max_ans = 0
        for j in range(1, len(A)):
            x = A[j]
            print(x)
            max_ans = max(max_ans, i + x - j)
            i = max(i, x + j)
        return max_ans
