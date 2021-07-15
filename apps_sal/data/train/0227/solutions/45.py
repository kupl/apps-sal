class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 

        # left - on the first 1 of the island
        # right - on the last 1 of that island
        left = 0
        while left < len(nums) and nums[left] != 1:
            left += 1

        right = left 
        while right + 1 < len(nums) and nums[right + 1] == 1:
            right += 1

        if right == len(nums):
            return 0

        maxOnes = right - left + 1

        while left < len(nums):
            left = right + 1
            while left < len(nums) and nums[left] != 1:
                left += 1

            right = left 
            while right + 1 < len(nums) and nums[right + 1] == 1:
                right += 1

            maxOnes = max(maxOnes, right - left + 1)

        return maxOnes
    
    
    def longestOnes(self, A: List[int], K: int) -> int:
        if K == 0:
            return self.findMaxConsecutiveOnes(A)
        
        if len(A) == 0:
            return 0

        left, right = 0, 0

        # Pre-condition: In the [left, right] we have exactly K zeros,
        # and you can't move right any more

        # Move right to K-th zero
        if A[right] == 0:
            K -= 1
        while right + 1 < len(A) and K > 0:
            right += 1
            if A[right] == 0:
                K -= 1

        # Move more if there are 1s to the right of K-th zero    
        while right + 1 < len(A) and A[right + 1] == 1:
            right += 1

        maxSize = right - left + 1

        while right < len(A):
            # Move left off of a zero, and then move right accordingly to include 1 more zero
            while left < len(A) and A[left] != 0:
                left += 1
            if left < len(A):
                left += 1
            else:
                return maxSize


            # Move right to include one more zero   
            right += 1
            while right + 1 < len(A) and A[right + 1] == 1:
                right += 1

            maxSize = max(maxSize, right - left + 1)
            
        return maxSize 
