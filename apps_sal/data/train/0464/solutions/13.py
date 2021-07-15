class Solution:
    def minOperations(self, n: int) -> int:
        res=0
        for i in range(n//2):
            res+=abs(2*i+1-n)
        return res
