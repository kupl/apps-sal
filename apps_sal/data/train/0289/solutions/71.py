class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        prefixSum = [0]  * (len(A)+1)
        for i in range(1, len(A)+1):
            prefixSum[i] = prefixSum[i-1] + A[i-1]
            
        # print(prefixSum)
        # print(M, L)
        ans = 0
        for i in range(M-1, len(A)):
            # print('i', i, i-(M-1))
            sumM = prefixSum[i+1] - prefixSum[i+1-M]
            sumL = 0
            for j in range(L-1, i-(M-1)):
                sumL = max(sumL, prefixSum[j+1] - prefixSum[j+1-L])
            # print('sumleft', sumL, L-1, i-(M-1))
            for j in range(i+1+L-1, len(A)):
                sumL = max(sumL, prefixSum[j+1] - prefixSum[j+1-L])
            # print('sumright', sumL)
            # print('sumM', sumM)
            ans = max(ans, sumM + sumL)
        return ans

