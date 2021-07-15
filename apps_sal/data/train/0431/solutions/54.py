class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        s=[]
        n = len(A)
        left =[1]*n
        right = [1]*n
        for i in range(n):
            while len(s)>0 and s[-1][0]>=A[i]:
                val, cnt = s.pop()
                left[i] += cnt
            s.append([A[i], left[i]])
            
        s = []
        for i in range(n-1, -1, -1):
            while len(s)>0 and s[-1][0]>A[i]:
                val, cnt = s.pop()
                right[i] += cnt
            s.append((A[i], right[i]))
            
        total = 0
        for a, l, r in zip(A, left, right):
            total += a*l*r
        return total%(10**9 + 7)
