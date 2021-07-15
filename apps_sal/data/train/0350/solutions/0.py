from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        
        start_k = 0
        start = 0
        elem_dict = defaultdict(int)
        
        ans = 0
        
        for elem in A:
            elem_dict[elem] += 1
            
            if len(elem_dict) > K:
                del elem_dict[A[start_k]]
                start_k+=1
                start = start_k
                
                
            if len(elem_dict) == K:
                while elem_dict[A[start_k]] > 1:
                    elem_dict[A[start_k]]-=1
                    start_k+=1
                    
                ans = ans + start_k - start + 1
                
        return ans
                
                
                

