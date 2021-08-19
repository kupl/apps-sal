from typing import List
from collections import Counter
import heapq


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        element_count = Counter(arr)
        count_heap = []
        for (element, count) in element_count.most_common():
            heapq.heappush(count_heap, [count, element])
        while k > 0:
            (curr_count, curr_elem) = heapq.heappop(count_heap)
            if k < curr_count:
                curr_count -= k
                k = 0
                heapq.heappush(count_heap, [curr_count, curr_elem])
            elif k > curr_count:
                k -= curr_count
            else:
                k = 0
        return len(count_heap)
