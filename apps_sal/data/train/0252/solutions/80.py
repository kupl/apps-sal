class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
#         taps=[]
#         for i in range(len(ranges)):
#             taps.append((i-ranges[i],i+ranges[i]))
        
#         taps.sort()
#         @lru_cache(None)
#         def helper(i):
#             # minimum number of taps to open if we open i to reach end
#             if i>=n+1:return float('inf')
#             if taps[i][1]>=n:return 1
#             ans=float('inf')
#             # lets do binary search here
#             start=i+1
#             end=n
#             lastindex=-1
#             # get the last index which is smaller than taps[i][1]
#             while start<=end:
#                 mid=start+(end-start)//2
#                 if taps[mid][0]<=taps[i][1]:
#                     lastindex=mid
#                     start=mid+1
#                 else:
#                     end=mid-1
#             if lastindex==-1:return ans
#             for j in range(i+1,lastindex+1):
#                 if taps[j][0]>taps[i][1]:
#                     break
#                 if taps[j][0]<=taps[i][1] and taps[j][1]>taps[i][1]:
#                     # benefit of picking this guy
#                     ans=min(ans,1+helper(j))
                    
#             # sequential code to do that
#             # dont go for binary unless interviewer say so
#             # ask him in the approach if he wants to
            
#             # for j in range(i+1,n+1):
#             #     if taps[j][0]>taps[i][1]:
#             #         break
#             #     if taps[j][0]<=taps[i][1] and taps[j][1]>taps[i][1]:
#             #         # benefit of picking this guy
#             #         ans=min(ans,1+helper(j))
#             return ans
#         ans=float('inf')
#         for i in range(n,-1,-1):
#             res=helper(i)
#             if taps[i][0]<=0 and res<ans:
#                 ans=res
#         return -1 if ans==float('inf') else ans
    
        best = [float('inf') for _ in ranges]
        for i, r in enumerate(ranges):
            if r > 0:
                start, end = i - r, i + r 
                best_with = 1 + (best[start] if start > 0 else 0)
                for j in range(max(0, start), min(len(ranges), end+1)):
                    best[j] = min(best[j], best_with)
        if any(v for v in best if v == float('inf')):
            return -1 
        return best[-1]
                
        
            
        
                    
                    
                    
                
            
        

