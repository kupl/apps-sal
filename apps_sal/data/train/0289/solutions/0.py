class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        N = len(A)
        if L + M > N:
            return -1

        def findmax(L, M):
            sL = [sum(A[:L])]
            for i in range(L, N - M):
                tmp = sL[-1] + A[i] - A[i - L]
                sL.append(tmp)
            sLmax = [sL[0]]
            for i in range(1, len(sL)):
                if sL[i] > sLmax[-1]:
                    sLmax.append(sL[i])
                else:
                    sLmax.append(sLmax[-1])

            sM = [sum(A[-M:])]
            for i in range(N - M - 1, L - 1, -1):
                tmp = sM[-1] + A[i] - A[i + M]
                sM.append(tmp)
            sMmax = [sM[0]]
            for i in range(1, len(sM)):
                if sM[i] > sMmax[-1]:
                    sMmax.append(sM[i])
                else:
                    sMmax.append(sMmax[-1])

            sMax = [sum(x) for x in zip(sLmax, sMmax[::-1])]
            m = max(sMax)

            return m

        if L == M:
            return findmax(L, M)
        else:
            return max(findmax(L, M), findmax(M, L))
