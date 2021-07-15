class Solution:
    def minOperations(self, a: List[int]) -> int:
        ans=0
        mx=0
        for x in a:
            cnt=0
            while x:
                if x%2:
                    ans+=1
                cnt+=1
                x//=2
            mx=max(mx,cnt)
        # print(ans,mx)
        return max(ans+mx-1,0)
