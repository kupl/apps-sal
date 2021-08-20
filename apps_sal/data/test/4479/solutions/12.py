class Solution:

    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        newA = sorted(A)
        print(newA)
        count = 0
        for i in range(K):
            newA[0] = -newA[0]
            newA = sorted(newA)
        print(newA)
        return sum(newA)
