class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        i_sum = []
        j_sum = []
        prev = -float('inf')
        max_sum = -float('inf')
        for i in reversed(list(range(len(A)))):
            if i > 0:
                if A[i] - i > prev:
                    j_sum.append(A[i] - i)
                    prev = A[i] - i
                else:
                    j_sum.append(prev)
            i_sum.append(A[i] + i)
        for i in reversed(list(range(1, len(i_sum)))):
            max_sum = max(max_sum, i_sum[i] + j_sum[i - 1])
        return max_sum
