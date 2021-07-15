class Solution:
    def minOperations(self, n: int) -> int:
        # array is like 1, 3, 5, 7, 9....
        #               2     5     8
        #               3           7
        #               4           6
        #               5           5
        
        # 2 6 3 5 4 4
        # diff / 2
        # array is like 1 3 5 7
        #                      
        if n == 1:
            return 0

        # one pair is difference divided by 2
        low = 0
        hi = n - 1
        num_ops = 0
        while low < hi:
            min_num = (2 * low) + 1
            max_num = (2 * hi) + 1

            num_ops += (max_num - min_num) // 2
                
            low += 1
            hi -= 1
            
        return num_ops
