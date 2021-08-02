class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:

        for i in range(K):

            val = min(A)

            # if val <= 0:
            A.remove(val)
            A.append(-1 * val)

        return sum(A)
