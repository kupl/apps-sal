class Solution:

    def minOperations(self, nums: List[int]) -> int:
        result = 0
        while True:
            to_continue = False
            ops = 0
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue
                elif nums[i] % 2 == 1:
                    nums[i] -= 1
                    ops += 1
                    to_continue = True
                else:
                    to_continue = True
            if ops > 0:
                result += ops
            elif to_continue:
                result += 1
                for i in range(len(nums)):
                    nums[i] //= 2
            else:
                break
        return result
