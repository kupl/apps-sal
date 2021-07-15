class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        left = [0]*len(A)
        right = [0]*len(A)
        s1, s2 = [], []
        for i in range(len(A)):
            count = 1
            while s1 and s1[-1][0]>A[i]:
                count+=s1.pop()[1]
            s1.append([A[i],count])
            left[i]=count
        for i in range(len(A))[::-1]:
            count = 1
            while s2 and s2[-1][0]>=A[i]:
                count+=s2.pop()[1]
            s2.append([A[i],count])
            right[i]=count
        ret = 0
        for i in range(len(A)):
            ret+=A[i]*(left[i]*right[i])
        return ret%(10**9+7)
                
            
                

