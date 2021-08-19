class Solution:

    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        for i in range(K):
            variable = min(A)
            A.remove(variable)
            A.append(variable * -1)
        return sum(A)
