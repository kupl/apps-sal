class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        L = len(A)
        res = 0
        if L<3:
            return 0
        if L==3:
            return 3 if A[0]+A[1]==A[2] else 0
        s = set(A)
        for i in range(2,L):
            for j in range(i):
                L,R = A[j],A[i]
                cur = 2
                while R-L in s and R-L<L:
                    cur += 1
                    L,R = R-L,L
                res = max(res,cur)
                
                #print(A[i],A[j],cur)
        return res if res>2 else 0
