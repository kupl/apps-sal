class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_count = 0
        front = 0
        back = 0
        prod = 1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                nums[i] = 1
            elif nums[i] < 0:
                nums[i] = -1
        
        while back < len(nums):
            if nums[back] == 0:
                back -= 1
                while front <= back and front < len(nums):
                    if nums[front] != 0:
                        prod /= nums[front]
                        front += 1
                        if prod > 0:
                            max_count = max(max_count, back - front + 1)
                    else:
                        front += 1
                
                front += 1
                back = front
                
            else:
                prod *= nums[back]
                if prod > 0:
                    max_count = max(max_count, back - front + 1)
                back += 1
        
        back -= 1
        while front <= back and front < len(nums):
            if nums[front] != 0:
                prod /= nums[front]
                front += 1
                if prod > 0:
                    max_count = max(max_count, back - front + 1)
            else:
                front += 1

                    
        return max_count
