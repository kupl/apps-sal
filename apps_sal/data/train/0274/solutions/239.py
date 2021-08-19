class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = deque()
        maxQ = deque()
        ans = -1
        l = 0
        for r in range(len(nums)):
            while minQ and nums[r] < minQ[-1]:
                minQ.pop()
            while maxQ and nums[r] > maxQ[-1]:
                maxQ.pop()
            minQ.append(nums[r])
            maxQ.append(nums[r])
            while abs(maxQ[0] - minQ[0]) > limit:
                if minQ and minQ[0] == nums[l]:
                    minQ.popleft()
                if maxQ and maxQ[0] == nums[l]:
                    maxQ.popleft()
                l += 1
            ans = max(ans, r - l + 1)
        return ans
