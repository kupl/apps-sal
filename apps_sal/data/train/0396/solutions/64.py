class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        N = 1
        for i in range(1, K+1):
            rem = N%K
            if rem==0:
                return i
            
            N = 10*rem+1
            
        return -1

