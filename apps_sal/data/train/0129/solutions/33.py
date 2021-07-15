class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        idx = [0]
        for i in range(1, len(A)):
            if A[i]+i-idx[-1]> A[idx[-1]]:
                idx.append(i)
        res = float('-inf')
        i = 1 
        j = 0
        #print(idx)
        while i < len(A):
            if j+1 < len(idx) and idx[j+1] < i:
                j += 1            
            res = max(res, A[i]+A[idx[j]]+idx[j]-i)
            i += 1
        return res
            

