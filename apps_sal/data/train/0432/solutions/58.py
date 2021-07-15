from typing import List

from collections import Counter, OrderedDict

class Solution:
    def can_process(self, sorted_counter, element, size):
        for i in range(element, element+size):
            if i not in sorted_counter:
                return False
        return True

    def process(self, queue, sorted_counter, element, size):
        for i in range(element, element+size):
            sorted_counter[i] -= 1

            if sorted_counter[i] == 0:
                del sorted_counter[i]
                queue.pop(0)

        return queue, sorted_counter

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        #O(nlogn) + O(n)
        sorted_counter = OrderedDict(Counter(sorted(nums)))

        #O(n) | S(unique(n))
        queue = list(sorted_counter.keys())

        #O(n)
        while len(queue):
            element = queue[0]
            if not self.can_process(sorted_counter, element, k):
                return False

            queue, sorted_counter = self.process(queue, sorted_counter, element, k)

        return True
