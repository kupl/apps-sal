class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0

        while True:
            next_nums = [0] * len(nums)
            all_zeros = True
            for i, x in enumerate(nums):
                if x == 0:
                    continue

                if x % 2 != 0:
                    count += 1

                next_num = x // 2
                next_nums[i] = next_num

                all_zeros &= next_num == 0

            if all_zeros:
                break

            count += 1
            nums = next_nums

        return count
