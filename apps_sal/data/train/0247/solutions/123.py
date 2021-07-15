class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        nums=[0 for i in range(len(arr))]
        nums[0]=arr[0]
        for i in range(1,len(arr)):
            nums[i]=nums[i-1]+arr[i]
        best=[float('inf') for i in range(len(arr))]
        ans=float('inf')
        size=float('inf')
        # count=2
        l=0
        r=0
        window=0
        while l<=r and r<len(arr):
            
            window+=arr[r]
            while l<=r and window>target:
                # print(l,r)
                window-=arr[l]
                
                l+=1
                
            if window==target:
                ans=min(ans,r-l+1+best[l-1])
                best[r]=min(best[r-1],r-l+1)
                      
            else:
                best[r]=best[r-1]
                
            r+=1
            
            
        
        if ans==float('inf'):
            return -1
        
        else:
            return ans
                
                
        
        
        
        
        
        
#         dp=[0 for i in range(len(arr)+1)]
        
#         currSum=0
#         l=[]
#         i=0
#         j=0
        
#         while i<=j and j<len(arr):
            
#             currSum=currSum+arr[j]
#             print(i,j,currSum)
#             if currSum==target or arr[j]==target:
#                 l.append(j-i+1)
#                 currSum=0
#                 j+=1
#                 i=j
                
#             elif currSum<target:
#                 currSum+=arr[j]
#                 j+=1
                
#             else:
#                 # print(\"h\",currSum)
#                 currSum=currSum-arr[i]
#                 # print(currSum,arr[i])
#                 i+=1
                
#         print(l)

