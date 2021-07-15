# class Solution:
#     def subarraysWithKDistinct(self, s: List[int], k: int) -> int:
#         # [1,2,1,2,3], K=2
#         #  ^
#         #    ^
#         #  3
#         n=len(s)
#         if n<k:
#             return 0
        
#         if k==0:
#             return 1
        
#         seen={}
#         cnt=0
        
#         i=0
#         j=0
        
#         while i<n and j<n:
#             if s[j] not in seen:
#                 seen[s[j]]=1
#             else:
#                 seen[s[j]]+=1
            
#             while len(seen)>k:
#                 seen[s[i]]-=1
#                 if not seen[s[i]]:
#                     del seen[s[i]]
#                 i+=1
                
#             seen1=seen.copy()
#             i1=i   
#             while len(seen1)==k:
#                 cnt+=1
#                 seen1[s[i1]]-=1
#                 if not seen1[s[i1]]:
#                     del seen1[s[i1]]
#                 i1+=1
                
#             j+=1

#         return cnt
class Window:
    def __init__(self):
        self.count = collections.Counter()
        self.nonzero = 0

    def add(self, x):
        self.count[x] += 1
        if self.count[x] == 1:
            self.nonzero += 1

    def remove(self, x):
        self.count[x] -= 1
        if self.count[x] == 0:
            self.nonzero -= 1

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        window1 = Window()
        window2 = Window()
        ans = left1 = left2 = 0

        for right, x in enumerate(A):
            window1.add(x)
            window2.add(x)

            while window1.nonzero > K:
                window1.remove(A[left1])
                left1 += 1

            while window2.nonzero >= K:
                window2.remove(A[left2])
                left2 += 1

            ans += left2 - left1

        return ans                
                    
                
                
            
        
        
        
        

