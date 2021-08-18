class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        max_list = []
        min_list = []

        j = 0

        for i in range(len(nums)):

            while max_list and max_list[-1] < nums[i]:
                max_list.pop()
            while min_list and min_list[-1] > nums[i]:
                min_list.pop()

            max_list.append(nums[i])
            min_list.append(nums[i])

            if max_list[0] - min_list[0] > limit:

                if max_list[0] == nums[j]:
                    max_list = max_list[1:]
                if min_list[0] == nums[j]:
                    min_list = min_list[1:]

                j += 1

        return len(nums) - j
