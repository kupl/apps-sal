class Solution:

    def numTriplets(self, A: List[int], B: List[int]) -> int:
        countA = defaultdict(int)
        countB = defaultdict(int)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                countA[A[i] * A[j]] += 1
        for i in range(len(B)):
            for j in range(i + 1, len(B)):
                countB[B[i] * B[j]] += 1
        res = 0
        for i in range(len(A)):
            val = A[i] ** 2
            res += countB[val]
        for i in range(len(B)):
            val = B[i] ** 2
            res += countA[val]
        return res
