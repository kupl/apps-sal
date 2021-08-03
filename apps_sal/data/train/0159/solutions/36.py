from typing import List
import collections


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        maxx = list(nums)
        deque = collections.deque()
        for i in range(len(nums)):
            if deque:
                maxx[i] += deque[0]
            while deque and maxx[i] > deque[-1]:
                deque.pop()
            if maxx[i] > 0:
                deque.append(maxx[i])
            if i >= k and deque and deque[0] == maxx[i - k]:
                deque.popleft()
        return max(maxx)
