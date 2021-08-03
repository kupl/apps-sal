class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        ma = 0
        for n in nums:
            k = 0
            while(n != 0):
                if(n % 2 == 0):
                    k += 1
                    n = n // 2
                else:
                    n -= 1
                    ans += 1
                ma = max(ma, k)
        return ans + ma
