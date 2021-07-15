class Solution:
    def minOperations(self, n: int) -> int:
        half = n//2
        half_list = [x for x in range(1,n,2)]
        return half*n - sum(half_list)
