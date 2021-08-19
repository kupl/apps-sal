class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = collections.deque()
        minq = collections.deque()
        start = 0
        for (i, n) in enumerate(nums):
            while maxq and maxq[-1][0] < n:
                maxq.pop()
            while minq and minq[-1][0] > n:
                minq.pop()
            maxq.append([n, i])
            minq.append([n, i])
            if maxq[0][0] - minq[0][0] > limit:
                if maxq[0][0] == nums[start]:
                    maxq.popleft()
                if minq[0][0] == nums[start]:
                    minq.popleft()
                start += 1
        return len(nums) - start
