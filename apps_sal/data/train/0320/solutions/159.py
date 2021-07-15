class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        max_divide = 0
        res = 0
        for num in nums:
            cnt_divide = 0
            while num:
                if num%2==1:
                    res += 1
                    num-=1
                else:
                    num //=2
                    cnt_divide += 1
            max_divide = max(max_divide, cnt_divide)
            
        return res + max_divide
            
                

