class Solution:
    def minOperations(self, n: int) -> int:
        # [1] 1 => 0
        # [1,3] 2 => 1
        # [1,3,5] 3 => 2
        # [1,3,5,7] 4 => 1 + 3 = 4
        # [1,3,5,7,9] 5 => 2 + 4 = 6
        # [1,3,5,7,9,11] 6 => 1 + 3 + 5 = 9
        # [1,3,5,7,9,11,13] 7 => 2 + 4 + 6 = 12
        
        if n <= 1:
            return 0
        else:
            ops = 0
            for x in range(n-1,0, -2):
                ops += x
            return ops
            
            
        

