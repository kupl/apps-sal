class Solution:
    def numTriplets(self, A: List[int], B: List[int]) -> int:
        countA, countB = Counter(A), Counter(B)
        res = 0
        for i in range(len(A)):
            x = A[i] * A[i]
            for j in range(len(B)):
                if x % B[j] == 0 and x // B[j] in countB:
                    if B[j] * B[j] == x:
                        res += (countB[x // B[j]] - 1)
                    else:
                        res += countB[x // B[j]]
        for i in range(len(B)):
            x = B[i] * B[i]
            for j in range(len(A)):
                if x % A[j] == 0 and x // A[j] in countA:
                    if A[j] * A[j] == x:
                        res += (countA[x // A[j]] - 1)
                    else:
                        res += countA[x // A[j]]
        return res // 2
