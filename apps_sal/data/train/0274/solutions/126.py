class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if limit < 0:
            return 0
        (i, j) = (0, 1)
        res = 0
        (max_q, min_q) = (collections.deque(), collections.deque())
        max_q.append((0, nums[0]))
        min_q.append((0, nums[0]))
        while j < len(nums):
            if max_q[0][1] - min_q[0][1] <= limit:
                while max_q and nums[j] > max_q[-1][1]:
                    max_q.pop()
                while min_q and nums[j] < min_q[-1][1]:
                    min_q.pop()
                max_q.append((j, nums[j]))
                min_q.append((j, nums[j]))
                j += 1
            if max_q[0][1] - min_q[0][1] > limit:
                res = j - i - 1 if j - i - 1 > res else res
                (min_i, max_i) = (min_q[0][0], max_q[0][0])
                if min_i < max_i:
                    i = min_i + 1
                    min_q.popleft()
                else:
                    i = max_i + 1
                    max_q.popleft()
        return j - i if j - i > res else res
