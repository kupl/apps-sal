class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        moves =0
        while True:
            zeros = 0
            for i in range(n):
                if nums[i] % 2:
                    nums[i] -= 1
                    moves += 1
                    
            for i in range(n):
                if nums[i] == 0: zeros += 1
            if zeros == n:
                return moves
            
            for j in range(n):
                nums[j] //= 2
            moves += 1
            
                
                    
            

