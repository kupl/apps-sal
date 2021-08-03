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
        # print(arr)
        # interesting how would you go about solving this?
        # is there a greedy solution
        # so for example every non 0 elt in the array
        # need a +1 operation to make it non zero
        # if a value is odd and not one we need a min of
        # 3 operations to get to where it needs to be
        #
        # can cache number of ops probably
        # print(nums)
        ops_needed = 0
        check_ind = 0
        nums.sort(key=lambda x: -x)
        while any(n != 0 for n in nums):
            for ind, numb in enumerate(nums):
                if numb >= 1 and numb % 2 == 1:
                    ops_needed += 1
                    # print(\"odd: \", nums, ops_needed)
                    nums[ind] = nums[ind] - 1

            for numb in nums:
                if numb >= 1 and numb % 2 == 0:
                    ops_needed += 1
                    # print(\"even: \", nums, ops_needed)
                    for ind, elt in enumerate(nums):
                        nums[ind] = nums[ind] / 2
                    break

            check_ind += 1
            if check_ind > 100:
                break
            # nums.sort(key = lambda x: -x)
        return ops_needed


[3, 3]
[1, 5]
[2, 2]
