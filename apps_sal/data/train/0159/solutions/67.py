from collections import deque


class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        largest = deque()
        global_max = float('-inf')
        for (i, num) in enumerate(nums):
            if largest and largest[-1][1] < i - k:
                largest.pop()
            curr = num + max(0, largest[-1][0] if largest else 0)
            while largest and curr > largest[0][0]:
                largest.popleft()
            global_max = max(global_max, curr)
            largest.appendleft((curr, i))
        return global_max
