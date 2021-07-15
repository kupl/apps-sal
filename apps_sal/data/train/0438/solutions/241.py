from collections import Counter
from typing import List

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:        
        n = len(arr)
        last = -2        
        sizes = Counter()        
        starts, ends = {}, {}
            
        def dec_sizes(size):
            sizes[size] -= 1
            if sizes[size] <= 0:
                sizes.pop(size)
    
        for i, x in enumerate(arr):
            x -=1                        
            count = 1            
            start = x
            end = x
            
            left = x - 1
            if left >= 0 and left in ends:
                len_ = ends.pop(left)
                j = left - len_ + 1                
                starts.pop(j)
                start = j
                count += len_                
                dec_sizes(len_)
                            
            right = x + 1
            if right < n and right in starts:
                len_ = starts.pop(right)
                j = right + len_ - 1
                ends.pop(j)
                end = j
                count += len_
                dec_sizes(len_)
                
            starts[start] = count
            ends[end] = count                                             
            sizes[count] += 1
            
            if m in sizes:
                last = i
        
        return last + 1

