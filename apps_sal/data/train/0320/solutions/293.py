class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = 0
        while 1:
            temp_counter = 0
            bigger_than_zero = 0
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    temp_counter += 1
                    nums[i] -= 1
                if nums[i] > 0:
                    bigger_than_zero += 1
                    temp = bin(nums[i])
            counter += temp_counter
            if bigger_than_zero == 0 :
                return counter

            counter += 1
            for i in range(len(nums)):
                nums[i] //= 2
        return counter
