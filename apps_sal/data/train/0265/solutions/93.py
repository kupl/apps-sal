from collections import defaultdict
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
#         cum_sum=[0]
#         for i in range(len(nums)): cum_sum.append(cum_sum[-1]+nums[i])

#         mem=defaultdict(list)

#         for i in range(len(nums)+1):
#             mem[cum_sum[i]].append(i)

#         def binSearch(index):
#             arr=mem[cum_sum[index]-target]
#             right=len(arr)-1
#             left=0
#             best=None
#             while left<=right:
#                 mid=(left+right)//2
#                 if arr[mid]<index:
#                     best=arr[mid]
#                     left=mid+1
#                 else:
#                     right=mid-1
#             return best

#         dp=[0 for i in range(len(nums)+1)]
#         for i in range(1,len(nums)+1):
#             ind=binSearch(i)
#             s=0
#             if ind!=None:
#                 s=1+dp[ind]
#             dp[i]=max(dp[i-1],s)

#         return dp[-1]
        dp=[0 for i in range(len(nums)+1)]
        mp={}
        s=0
        mp[0]=0
        for i in range(1,len(nums)+1):
            s+=nums[i-1]
            dp[i]=dp[i-1]
            if s-target in mp:
                dp[i]=max(dp[i],1+dp[mp[s-target]])
            if nums[i-1]==target:
                dp[i]=max(dp[i],1+dp[i-1])
            mp[s]=i
        return dp[-1]



