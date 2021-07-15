class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        
        lenCount = 1
        curr = 1
        
        while curr % K != 0:
            curr = (curr * 10) + 1
            lenCount += 1
            
        return lenCount
