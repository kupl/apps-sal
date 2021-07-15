class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # encouter 0 reset it as 0
        # how many -1 in the left, if is even, update the  longest length O(n) cur_poistion - 0_position
        
        # [1,-2,-3,4] => [0, 1, 2, 2] => 4
        # [0,1,-2,-3,-4] => [0, 0, 1, 2, 3] => 3
        # [-1,-2,-3,0,1] => [1, 2, 3, 0, 0] => 2
        # [-1,2] => [1, 1] => 1 (consider if itself > 0, 1)
        # [1,2,3,5,-6,4,0,10] => [0, 0, 0, 0, 1, 1, 0, 1] => 4
        # [0, 0 ,0 ,0] => [0, 0, 0, 0] => 0 (consider if itself == 0, 0)
        
        carry_len = 0
        left_neg = 0
        max_len = 0
        str_ptr = -1
        for idx, n in enumerate(nums):
            if n < 0 :left_neg += 1 
            carry_len += 1
            if n == 0: 
                max_len = max(max_len, 0)
                carry_len = 0
                left_neg = 0
            else:
                max_len = max(max_len, 1 if n > 0 else 0, idx - str_ptr -1, carry_len if left_neg % 2 == 0 else 0)
            if left_neg == 0: 
                str_ptr = idx

        return max_len
