class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s=sum(A)
        if s%3!=0:
            return 0
        n=len(A)
        cnt=[0]*n
        s//=3
        ss=0
        for i in range(n-1,-1,-1):
            ss+=A[i]
            if i==n-1:
                cnt[i]= 1 if ss==s else 0
            else:
                cnt[i]=cnt[i+1]+ (1 if ss==s else 0)
        ss=0
        ans=0
        print(cnt)
        for i in range(0,n-2):
            ss+=A[i];
            if ss==s:
                ans+=cnt[i+2]
        print(ans)
        return True if ans>0 else False
