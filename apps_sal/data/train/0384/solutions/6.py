class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        
        # # N^2log(N) time over limit
        # aa = sorted(A)
        # n = len(A)
        # res = 0
        # # print(aa)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         res = (res+2**(j-i-1)*(aa[j]-aa[i]))%(10**9+7)
        #         # print(i,j,aa[i],aa[j],res)
        # return res
        
        # above simplified (simple math), NlogN time
        aa = sorted(A)
        n = len(A)
        res = 0
        # print(aa)
        md = 10**9 + 7
        p2 = [1]*n
        for i in range(1,n):
            p2[i] = (p2[i-1]*2) % md
        for i in range(n):
            res = (res+aa[i]*(p2[i]-p2[n-i-1])) % md
        return res

