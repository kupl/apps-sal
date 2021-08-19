class Solution:

    def numTriplets(self, A, B):
        countA = collections.Counter()
        countB = collections.Counter()
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                countA[A[i] * A[j]] += 1
        for i in range(len(B)):
            for j in range(i + 1, len(B)):
                countB[B[i] * B[j]] += 1
        ans = 0
        for x in A:
            ans += countB[x * x]
        for x in B:
            ans += countA[x * x]
        return ans
