import collections


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        sol = -float('inf')
        n = len(nums)
        maxque = collections.deque([(-1, 0)])
        for i in range(n):
            max_i = max(maxque[0][1], 0) + nums[i]
            sol = max(sol, max_i)
            while maxque:
                if maxque[-1][1] < max_i:
                    maxque.pop()
                else:
                    break
            maxque.append((i, max_i))
            if maxque[0][0] <= i - k:
                maxque.popleft()
        return sol
