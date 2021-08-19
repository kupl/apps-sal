from collections import deque


class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        (d, res) = (deque(), 0)
        d.append(-1)
        for i in range(0, len(nums)):
            if nums[i] % 2 == 1:
                d.append(i)
            if len(d) > k + 1:
                d.popleft()
            if len(d) == k + 1:
                a = d.popleft()
                b = d.popleft()
                res += b - a
                d.appendleft(b)
                d.appendleft(a)
        return res
