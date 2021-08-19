class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        resL = []
        resM = []
        for i in range(len(A) - L + 1):
            resL.append(sum(A[i:i + L]))
        for i in range(len(A) - M + 1):
            resM.append(sum(A[i:i + M]))
        print(resL)
        print(resM)
        i = 0
        maxValue = -1
        while i < len(resL):
            for j in range(i + L, len(resM)):
                maxValue = max(resL[i] + resM[j], maxValue)
            for j in range(min(i - M, len(resM))):
                maxValue = max(resL[i] + resM[j], maxValue)
            i += 1
        return maxValue
