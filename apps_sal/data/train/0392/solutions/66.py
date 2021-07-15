class Solution:
    
    # from collections import Counter
    
    CONST = 1_000_000_000 + 7
    
    def numWays(self, s: str) -> int:
        n = len(s)
        # edge cases 
        num_ones = 0
        for c in s:
            if c == '1':
                num_ones += 1        
        if num_ones % 3 != 0:
            return 0
        if num_ones == 0:
            return ((n-1) * (n-2) // 2) % self.CONST
        
        # general case 
        # \"100100010100110\"
        # 1001| 00010100110
        # 10010| 0010100110        
        # 100100| 010100110 
        # 1001000| 10100110
        
        # 0 0
        # 0 0
        # 0 0
        # 1 0
        # 2 0
        # 3 0
        # 4 0
        # 4 1
        # 4 2
        # 4 2
        # 4 2
        # 4 2
        # 4 2
        # 4 2
        # 4 2
        
        num_ones_per_chunk = num_ones // 3
        first, second = 0, 0
        num_ones_sofar = 0
        
        # dumb version
        for idx, c in enumerate(s):
            num_ones_sofar += c == '1'
            if num_ones_sofar < num_ones_per_chunk:
                pass
            elif num_ones_per_chunk <= num_ones_sofar < num_ones_per_chunk + 1:
                first += 1
            elif 2 * num_ones_per_chunk <= num_ones_sofar < 2 * num_ones_per_chunk + 1:
                second += 1
            else:
                pass
            # print(s[:idx+1])
            # print(first, second)
            # print('')
            
        # # smart version
        # for c in s:
        #     num_ones_sofar += c == '1'
        #     if num_ones_sofar == num_ones_per_chunk:
        #         first += 1
        #     elif num_ones_sofar == 2 * num_ones_per_chunk:
        #         second += 1
        
        # \"10101\"
        # \"1001\"
        # \"000000\"
        return (first * second) % self.CONST
            
            

