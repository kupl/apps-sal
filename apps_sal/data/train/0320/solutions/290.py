class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''        
        Instead of trying to go from 0 array to nums,
        go from nums to 0 array, decrement index by 1
        divide all elements by 2 if divisible by 2

        Nevermind this isn't DP, do greedy, divide by
        2 as much as possible then decrement indexes by 1

        Repeat until everything is divisble by 2 again 

        4 2 5 

        4 2 4  + 1

        2 1 2  + 1

        2 0 2  + 1

        1 0 1  + 1

        0 0 0  + 2
        '''
        ops = 0
        while not all(n == 0 for n in nums):
            for i, n in enumerate(nums):
                if n % 2 != 0:
                    nums[i] = n - 1
                    ops += 1

            if all(n == 0 for n in nums):
                break

            nums = [n // 2 for n in nums]
            ops += 1

        return ops
