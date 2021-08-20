class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        curr_max = deque([])
        curr_min = deque([])
        i = 0
        j = 0
        res = 0
        while i <= j and j < len(nums):
            num = nums[j]
            while curr_max and curr_max[-1] < num:
                curr_max.pop()
            else:
                curr_max.append(num)
            while curr_min and curr_min[-1] > num:
                curr_min.pop()
            else:
                curr_min.append(num)
            if curr_max[0] - curr_min[0] <= limit:
                res = max(res, j - i + 1)
            else:
                value = nums[i]
                if value == curr_max[0]:
                    curr_max.popleft()
                if value == curr_min[0]:
                    curr_min.popleft()
                i += 1
            j += 1
        return res
