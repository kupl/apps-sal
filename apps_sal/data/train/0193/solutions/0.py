from heapq import *
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        counter = Counter(arr)
        size = len(arr)
        
        # unique elements (remove half of them)
        if len(counter) == size:
            return (size - 1) // 2 + 1
        
        max_heap = [(-freq, value) for value, freq in list(counter.items())]
        heapify(max_heap)
        
        removed = 0  # number of elements removed
        removed_size = 0  # size of the remvoved set
        
        while removed < size//2:
            count, value = heappop(max_heap)
            count = -count  # change the count back to +ve
            removed += count
            removed_size += 1
        
        return removed_size
        
        

