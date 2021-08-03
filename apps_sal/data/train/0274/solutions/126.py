class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # [8, 2, 4, 7] limit = 4
        # want to keep track of max and min elements + indexes
        # thinking of a sliding window approach
        # 8, 8 -> 8, 2 -> 2, 4 -> 2, 7 -> end
        # difference between i and j + 1
        # [10, 1, 2, 4, 7, 2], limit = 5
        # 10, 10 -> 10, 1 -> 1, 2 -> 1, 4 -> 1, 7 -> 2, 7 -> 2, 2 -> end
        # turns out i need a list of max and min elements + indexes
        # [8, 11, 5, 7, 9, 10, 8, 7, 6];
        # (8, 11) -> (11, 5) ->
        # The list of max elements must contain elements in window, descending order
        # The list of min elements must contain elements in window, ascending order

        # (6, 8) (7, 7) (9, 6)
        # (9, 6)
        # i = 3, j = 10
        # res = 6

        if limit < 0:
            return 0

        i, j = 0, 1
        res = 0
        max_q, min_q = collections.deque(), collections.deque()
        max_q.append((0, nums[0]))
        min_q.append((0, nums[0]))
        while j < len(nums):
            if (max_q[0][1] - min_q[0][1] <= limit):
                while max_q and nums[j] > max_q[-1][1]:
                    max_q.pop()
                while min_q and nums[j] < min_q[-1][1]:
                    min_q.pop()
                max_q.append((j, nums[j]))
                min_q.append((j, nums[j]))
                j += 1
            if (max_q[0][1] - min_q[0][1] > limit):
                res = j - i - 1 if j - i - 1 > res else res
                min_i, max_i = min_q[0][0], max_q[0][0]
                if (min_i < max_i):
                    i = min_i + 1
                    min_q.popleft()
                else:
                    i = max_i + 1
                    max_q.popleft()
        return j - i if j - i > res else res
