from bisect import bisect

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        d = {float('-inf'): 0}
        arr2 = sorted(set(arr2))
        for i in arr1:
            d2 = {}
            for k, v in list(d.items()):
                if i > k:
                    if i in d2:
                        d2[i] = min(d2[i], v)
                    else:
                        d2[i] = v

                if k < arr2[-1]:
                    j = arr2[bisect(arr2, k)]
                    if j in d2:
                        d2[j] = min(d2[j], v + 1)
                    else:
                        d2[j] = v + 1
            
            d = d2
        
        if d:
            return min(d.values())
        return -1
                        
        
        
        
        

