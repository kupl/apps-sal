class Solution:
    def knightDialer(self, n: int) -> int:
        if(n == 0):
            return 0
        if(n == 1):
            return 10
        total = 9
        digit = {}
        for j in range(0,10):
            if(j == 5):
                continue
            digit[j] = 1
        const = 10 ** 9 + 7
        for i in range(1,n):
            num_1 = (digit[6] + digit[8]) % const
            num_2 = (digit[7] + digit[9]) % const
            num_3 = (digit[4] + digit[8]) % const
            num_4 = (digit[3] + digit[9] + digit[0]) % const
            num_6 = (digit[1] + digit[7] + digit[0]) % const
            num_7 = (digit[2] + digit[6]) % const
            num_8 = (digit[1] + digit[3]) % const
            num_9 = (digit[2] + digit[4]) % const
            num_0 = (digit[4] + digit[6]) % const
            digit[0] = num_0
            digit[1] = num_1
            digit[2] = num_2
            digit[3] = num_3
            digit[4] = num_4
            digit[6] = num_6
            digit[7] = num_7
            digit[8] = num_8
            digit[9] = num_9
            total = (num_0 + num_1 + num_2 + num_3 + num_4 + num_6 + num_7  + num_8 + num_9) % const
        return total
            
            

