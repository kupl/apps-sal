class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        s = set()
        for i in A:
            s.add(i)
        res = 0
        ll = 0
        for i in range(n):
            for j in range(i+1,n):
                f1 = A[i]
                f2 = A[j]
                if f1+f2 in s:
                    ll = 2
                while f1+f2 in s:
                    ll += 1
                    tmp = f2
                    f2 = f1+f2
                    f1 = tmp
                res = max(res,ll)
        return res
                    
                

