class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        
        k = 1
        count = 0
        while N / k - (k / 2) > 0:
            print(k)
            if k % 2 != 0 and N % k == 0:
                count += 1
            elif N / k == N // k + 0.5:
                count += 1
            k += 1
        return count
        
        #15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
        # 15 / 1 = 15
        # 15 / 2 = 7.5 = 8 + 7
        # 15 / 3 = 5 = 4+5+6
        # 15 / 4 = 3. 75 not use
        # 15 / 5 = 3    ( 3 - 5 / 2) > 0
        # 15 / 6 = 2.5    (2.5 - 6 / 2) < 0  not use

