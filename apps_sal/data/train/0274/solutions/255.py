class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        mindeq = deque()
        maxdeq = deque()

        i = 0
        ans = 1

        for j in range(0, len(nums)):

            while(len(maxdeq) > 0 and maxdeq[-1] < nums[j]):
                maxdeq.pop()

            maxdeq.append(nums[j])

            while(len(mindeq) > 0 and mindeq[-1] > nums[j]):
                mindeq.pop()

            mindeq.append(nums[j])

            if(maxdeq[0] - mindeq[0] > limit):
                if(maxdeq[0] == nums[i]):
                    maxdeq.popleft()
                if(mindeq[0] == nums[i]):
                    mindeq.popleft()
                i += 1

            ans = max(ans, j - i + 1)

        return ans
