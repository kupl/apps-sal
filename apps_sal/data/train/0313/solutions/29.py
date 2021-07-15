class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k: return -1
        
        
        
        
#         def helper(D_days):
#             n_m = 0
#             low = 0 
#             while low + k <= len(bloomDay):
#                 _range = bloomDay[low: low+k]
#                 isValid = True
#                 for fl in _range:
#                     if fl > D_days: 
#                         low += 1
#                         isValid = False
#                         break
#                 if isValid:
#                     n_m += 1
#                     low += k
                
#             if n_m < m: return +1
#             else: return -1
            
        def helper(D_days):
            n_m = 0
            n_k = 0

            for index, fl in enumerate(bloomDay):
                if fl > D_days:
                    n_k = 0
                else: 
                    n_k += 1

                if n_k == k: 
                    n_m +=1 
                    n_k = 0

            if n_m < m: return +1
            else: return -1

                        
            
#             low = 0 
#             while low + k <= len(bloomDay):
#                 _range = bloomDay[low: low+k]
#                 isValid = True
#                 for fl in _range:
#                     if fl > D_days: 
#                         low += 1
#                         isValid = False
#                         break
#                 if isValid:
#                     n_m += 1
#                     low += k
                
#             if n_m < m: return +1
#             else: return -1
    
            
    
                        
# Binary search   
        def B_search():
            low, high = 0, max(bloomDay)+1
            
            while low < high:
                mid = low + (high-low)//2
                
                if helper(mid)==+1:
                    low = mid +1
                else:
                    high = mid
                    
            return low
        
        return B_search()
                    

