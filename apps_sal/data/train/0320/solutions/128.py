class Solution:
    def minOperations(self, nums: List[int]) -> int:
#         # bit operation
#         # The number of operation 0 equals to the total number of bits \"1\".
#         # The number of operation 1 equals to maximum bit length - 1.
        
#         # operation 0: turning 1 to 0. make 1 bit to 0 bit. need 1 operation individually
#         # thus count number of 1 bits for each number and add them up
        
#         # operation 2: divide number by 2 -> shift 1 bit to right. this can be share with all numbers
#         # 1 step operation to shift all numbers to right by 1 bit.
#         # Thus find the number with max length of bit (max number in the array), count how many bits.
#         return sum(bin(a).count('1') for a in nums) + len(bin(max(nums))[2:]) - 1
    
    
        # sum of the addition operations and the maximum number of multiply operations in any element.
        # O(32N) = O(N)
        twos = 0
        ones = 0
        for n in nums:
            mul = 0
            while n:
                if n%2 == 1: # odd number, just delete 1 so that it's now a multiple of 2
                    n -= 1
                    ones += 1
                else: # multiple of 2, so just divide by 2 
                    n //= 2
                    mul += 1
            twos = max(twos, mul)
            
        return ones + twos

