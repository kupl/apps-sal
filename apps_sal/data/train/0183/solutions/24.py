class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp=[[0 for _ in range(len(nums2))] for _ in range(len(nums1))]
        
        dp[-1][-1]=nums1[-1]*nums2[-1]
        for i in range(len(nums1)-2,-1,-1):
            dp[i][-1]=max(dp[i+1][-1],nums1[i]*nums2[-1])
        
        for i in range(len(nums2)-2,-1,-1):
            dp[-1][i]=max(dp[-1][i+1],nums1[-1]*nums2[i])
        
        for i in range(len(nums1)-2,-1,-1):
            for j in range(len(nums2)-2,-1,-1):
                dp[i][j]=max(dp[i+1][j+1],dp[i+1][j],dp[i][j+1],dp[i+1][j+1]+(nums1[i]*nums2[j]),nums1[i]*nums2[j])
        return dp[0][0]
                
                
        
        
#         def backtrack(arr,ind,curr,sol):
#             if curr:
#                 sol[len(curr)-1].append(curr)
#             for i in range(ind,len(arr)):
#                 backtrack(arr,i+1,curr+[arr[i]],sol)
        
#         subs1=[[] for _ in range(len(nums1))]
#         subs2=[[] for _ in range(len(nums2))]
        
#         backtrack(nums1,0,[],subs1)
#         backtrack(nums2,0,[],subs2)
        
#         mx=float(\"-inf\")

#         for i in range(min(len(nums1),len(nums2))):
#             for j in range(len(subs1[i])):
#                 for k in range(len(subs2[i])):
#                     ans=0
#                     for l in range(i+1):
#                         ans+=subs1[i][j][l]*subs2[i][k][l]
#                     mx=max(mx,ans)
#         return mx
                        

