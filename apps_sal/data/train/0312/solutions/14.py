from typing import List
import heapq
import math


class Solution:
    def shortestSubarray(self, A: List[int], k: int) -> int:
        shortest = math.inf
        sum = 0
        # priority queue to store tuples (partial_sum, index_last_element)
        pq = []
        # we iterate over array
        for counter, value in enumerate(A):
            sum += value
            if sum >= k:
                shortest = counter + 1 if counter < shortest else shortest

            while pq and sum - pq[0][0] >= k:
                shortest = counter - pq[0][1] if counter - pq[0][1] < shortest else shortest
                heapq.heappop(pq)

            heapq.heappush(pq, (sum, counter))

        return shortest if shortest != math.inf else -1
