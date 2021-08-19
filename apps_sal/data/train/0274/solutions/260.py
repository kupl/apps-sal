class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = collections.deque()
        min_deque = collections.deque()
        n = len(nums)
        l = 0
        res = 0
        for r in range(n):
            self.push_max_deque(max_deque, nums, r)
            self.push_min_deque(min_deque, nums, r)
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if max_deque[0] == l:
                    max_deque.popleft()
                if min_deque[0] == l:
                    min_deque.popleft()
                l += 1
            res = max(res, r - l + 1)
        return res

    def push_max_deque(self, max_deque, nums, i):
        while max_deque and nums[max_deque[-1]] < nums[i]:
            max_deque.pop()
        max_deque.append(i)

    def push_min_deque(self, min_deque, nums, i):
        while min_deque and nums[min_deque[-1]] > nums[i]:
            min_deque.pop()
        min_deque.append(i)
