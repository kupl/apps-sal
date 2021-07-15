class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def calc(nums, divisor):
            s = 0
            for num in nums:
                if num % divisor == 0:
                    s += num // divisor
                else:
                    s += num // divisor + 1
            
            # print(divisor, s)
            return s
        
        left = 1
        right = sum(nums) // (threshold-1) + threshold*100
        print((left, right))
        
        while left < right:
            mid = (left+right) // 2
            
            cur_res = calc(nums, mid)
            if cur_res > threshold:
                left = mid + 1
            else:
                right = mid
        
        return left
                

