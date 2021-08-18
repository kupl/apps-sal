class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def modify(arr, op, ind):
            if op == 0:
                arr[ind] = arr[ind] + 1
            if op == 1:
                for i in range(len(arr)):
                    arr[i] = arr[i] * 2
            return arr

        arr = [0] * n
        ops_needed = 0
        check_ind = 0
        nums.sort(key=lambda x: -x)
        while any(n != 0 for n in nums):
            for ind, numb in enumerate(nums):
                if numb >= 1 and numb % 2 == 1:
                    ops_needed += 1
                    nums[ind] = nums[ind] - 1

            for numb in nums:
                if numb >= 1 and numb % 2 == 0:
                    ops_needed += 1
                    for ind, elt in enumerate(nums):
                        nums[ind] = nums[ind] / 2
                    break

            check_ind += 1
            if check_ind > 100:
                break
        return ops_needed
