class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        count_of_negative = 0
        start = 0
        max_length = 0

        def evaluate_sub_array(begin, end, count_of_negative):
            if count_of_negative % 2 == 0:
                return end - begin + 1
            else:
                first_negative = len(nums)
                last_negative = -1
                for i in range(begin, end + 1):
                    if nums[i] < 0:
                        if first_negative == len(nums):
                            first_negative = i
                            last_negative = i
                        else:
                            last_negative = i
            return max(end - first_negative, last_negative - begin)

        start = 0
        array = []
        count_of_negative = 0
        for index in range(len(nums)):
            if nums[index] < 0:
                count_of_negative += 1
            if nums[index] == 0:
                array.append(evaluate_sub_array(start, index - 1, count_of_negative))
                count_of_negative = 0
                start = index + 1
        array.append(evaluate_sub_array(start, len(nums) - 1, count_of_negative))
        return max(array)
