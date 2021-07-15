class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        l, r = [None]*len(A), [None]*len(A)
        s1, s2 =[], []
        for i in range(len(A)):
            c = 1
            while s1 and (s1[-1][0]>= A[i]):
                c += s1[-1][1]
                s1.pop(-1)
                
            s1.append([A[i], c])
            l[i] = c
            
        for i in range(len(A)-1, -1, -1):
            c = 1
            while s2 and(s2[-1][0] > A[i]):
                c += s2[-1][1]
                s2.pop(-1)
            s2.append([A[i], c])
            r[i] = c
        result = 0
        
        for i in range(len(A)):
            result += A[i]*l[i]*r[i]
        return result%(10**9 + 7)
    

