from collections import deque


class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums.append(1)
        odds = deque()
        odds.append(-1)
        total = 0
        for (i, val) in enumerate(nums):
            if val % 2:
                odds.append(i)
                if len(odds) > k + 2:
                    odds.popleft()
                if len(odds) == k + 2:
                    total += (odds[1] - odds[0]) * (odds[-1] - odds[-2])
        return total
