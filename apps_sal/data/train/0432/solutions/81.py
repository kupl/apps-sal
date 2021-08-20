from collections import Counter
from heapq import heappop, heapify


def is_possible_divide(heap, k):
    if len(heap) == 0:
        return True
    else:
        popped = []
        (prev, min_count) = heappop(heap)
        for i in range(k - 1):
            if not heap:
                return False
            else:
                (value, count) = heappop(heap)
                if value != prev + 1:
                    return False
                else:
                    count -= min_count
                    prev = value
                if count > 0:
                    popped.append((value, count))
        heap.extend(popped)
        heapify(heap)
        return is_possible_divide(heap, k)


class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        heap = [(value, count) for (value, count) in list(Counter(nums).items())]
        heapify(heap)
        return is_possible_divide(heap, k)
