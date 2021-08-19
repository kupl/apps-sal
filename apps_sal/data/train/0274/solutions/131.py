class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = collections.deque()
        max_deque = collections.deque()

        l = 0
        ans = 0
        for r, num in enumerate(nums):
            while(min_deque and nums[min_deque[-1]] >= num):
                min_deque.pop()
            while(max_deque and nums[max_deque[-1]] <= num):
                max_deque.pop()

            min_deque.append(r)
            max_deque.append(r)

            while(nums[max_deque[0]] - nums[min_deque[0]] > limit):
                l += 1
                while(max_deque[0] < l):
                    max_deque.popleft()
                while(min_deque[0] < l):
                    min_deque.popleft()

            ans = max(ans, r - l + 1)
            # print(\"iteration\")
            # print(r)
            # print(ans)
            # print(r - l + 1)

        return ans
