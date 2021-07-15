class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        d1=collections.defaultdict(int)
        d2=collections.defaultdict(int)

        N=len(A)
        MOD=10**9+7
        cnt = 0
        for i in range(N-1,-1,-1):
            n=A[i]
            cnt+=d2[target-n]
            cnt%=MOD
            for (nn, nncnt) in list(d1.items()):
                d2[nn+n]+=nncnt

            d1[n]+=1

        return cnt
            

