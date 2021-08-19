class Solution:

    def countTriplets(self, A: List[int]) -> int:
        cnt = 0
        d = {}
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i] & A[j] not in d:
                    d[A[i] & A[j]] = 1
                else:
                    d[A[i] & A[j]] += 1
        for i in range(len(A)):
            for j in d:
                if A[i] & j == 0:
                    cnt += d[j]
        return cnt
