class Solution(object):
    def numTriplets(self, A, B):
        from collections import Counter
        countA = Counter()
        countB = Counter()
        for i, x in enumerate(A):
            for j in range(i+1, len(A)):
                y = A[j]
                countA[x * y] += 1
        for i, x in enumerate(B):
            for j in range(i+1, len(B)):
                y = B[j]
                countB[x * y] += 1
        ans = 0
        for i, x in enumerate(A):
            ans += countB[x * x]
        for i, x in enumerate(B):
            ans += countA[x * x]
        return ans
