class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''Reverse thinking, from result number back to zeros'''
        '''Time:O(n*n/2)->O(n^2), Space:O(1)'''
#         result = 0
#         zeros = 0
#         for n in nums:
#             if n==0:
#                 zeros+=1
                
#         #when all numbers are even, /2
#         #when there is any odd number, -1
#         while zeros<len(nums):
#             for i in range(len(nums)):
#                 if nums[i]%2!=0:
#                     nums[i]-=1
#                     result+=1
#                     if nums[i]==0:
#                         zeros+=1
#                     # print('odd')
#             if zeros==len(nums):
#                 break
                
#             flag=0
#             for j in range(len(nums)): 
#                 if j==0:
#                     flag=1
#                 nums[j]/=2  
#                 if flag==1:
#                     result += 1
#                     flag=0
#                     # print('even')
                    
#         return result

        '''Time:O(n), Space:O(1)'''
        twos = 0
        ones = 0
        for n in nums:
            mul = 0
            while n:
                if n%2:
                    n -= 1
                    ones += 1
                else:
                    n //= 2
                    mul += 1
            twos = max(twos, mul)
        return ones + twos
