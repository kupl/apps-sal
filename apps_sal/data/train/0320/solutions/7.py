class Solution:
    def minOperations_1(self, nums: List[int]) -> int:
        '''        
        Instead of trying to go from 0 array to nums,
        go from nums to 0 array, decrement index by 1
        divide all elements by 2 if divisible by 2

        Nevermind this isn't DP, do greedy, divide by
        2 as much as possible then decrement indexes by 1

        Repeat until everything is divisble by 2 again

        Runtime?

        O(3n) inner loop, 32 times outer loop because
        divison by 2 happens frequently which shifts
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

    def minOperations_2(self, nums: List[int]) -> int:
        '''
        More efficient way to do this:

        Loop through the numbers individually, count
        the number of times you have to subtract 1 and divide
        by 2. Add 1's to total but only take the maximum number
        of times to divide by 2 since division affects everything
        and so only the largest number of divisions gets taken
        into account

             24 2 5 

        ones  2 1 2

        twos  4 1 2

        5 + max(twos) = 9
        '''
        op_1 = 0
        op_2 = 0
        for n in nums:
            op_2_cur = 0
            while n > 0:
                if n % 2 != 0:
                    op_1 += 1
                    n -= 1
                else:
                    op_2_cur += 1
                    n = n // 2

            op_2 = max(op_2, op_2_cur)

        return op_1 + op_2

    def minOperations(self, nums: List[int]) -> int:
        '''
        Bit Manipulation Solution (Most Efficient)

        Multiplying by 2 is equivalent to bit shift to left by 1
        Likewise divide by 2 is equivalent to bit shift to right by 1

        Using this knowledge, the highest leftmost bit will determine
        how many divide by 2 operations we have to perform

        24

        11000 => 4 operations

        The number of 1's in the number determine the number of 1 operations
        to perform

        24
        11000 => 2 operations

        We loop from bit to bit to avoid the max comparison operation

        O(32n) Time, O(1) Space

        -----------------------------------------

        (n & (1 << i)) != 0

        Gets bit at index i in the number

        Ex. Get index 4

          4 3 2 1 0

          1 1 0 0 0
        & 1 0 0 0 0
        -----------
          1 0 0 0 0

        Final result not 0 so index 4 must've been a 1

          4 3 2 1 0

          0 1 0 0 0
        & 1 0 0 0 0
        -----------
          0 0 0 0 0

        If index 4 was 0 then result would be all 0's
        '''
        op1 = 0
        op2 = 0
        for i in range(31):
            for n in nums:
                if (n & (1 << i)) != 0:
                    op1 += 1
                    op2 = i

        return op1 + op2
