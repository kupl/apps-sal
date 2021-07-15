class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n,ans=len(nums),0
        zeros,cn,prev={i:[-1,n,0,0] for i in range(n)},0,-1
        for i in range(n):
            zeros[i][0]=prev
            zeros[i][2]=cn
            if nums[i]==0:
                prev=i
                cn=0
            if nums[i]<0:
                cn+=1
        cn,prev=0,n
        for i in range(n-1,-1,-1):
            zeros[i][1]=prev
            zeros[i][3]=cn
            if nums[i]==0:
                prev=i
                cn=0
            if nums[i]<0:
                cn+=1
        for i in range(n):
            if nums[i]==0:
                if zeros[i][2]%2==0:
                    ans=max(ans,i-zeros[i][0]-1)
                if zeros[i][3]%2==0:
                    ans=max(ans,zeros[i][1]-i-1)
            elif nums[i]<0:
                if zeros[i][2]%2==0:
                    ans=max(ans,i-zeros[i][0]-1)
                else:
                    ans=max(ans,i-zeros[i][0])
                if zeros[i][3]%2==0:
                    ans=max(ans,zeros[i][1]-i-1)
                else:
                    ans=max(ans,zeros[i][1]-i)
            else:
                if zeros[i][2]+zeros[i][3]%2==0:
                    ans=max(ans,zeros[i][1]-zeros[i][0]-1)
                elif zeros[i][2]%2==0:
                    ans=max(ans,i-zeros[i][0])
                elif zeros[i][3]%2==0:
                    ans=max(ans,zeros[i][1]-i)
            if ans==n: break
        return ans
