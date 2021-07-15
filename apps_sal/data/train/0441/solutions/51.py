class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        if not N:
            return 0
        
        count = 0
        idx = 1
        while (idx*(idx+1)//2 <= N):
            if (N - idx*(idx+1)//2) % idx == 0:
                count += 1
            idx += 1
        return count
        

