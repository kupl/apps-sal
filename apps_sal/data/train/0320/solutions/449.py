class Solution:
    def minOperations(self, nums: List[int]) -> int:
        import sys
        import math

        def h2(n):
            ans1 = 0
            ans2 = 0
            while(n != 1):
                if(n % 2 == 0):
                    ans1 += 1
                    n /= 2
                else:
                    n -= 1
                    ans2 += 1
            return ans1, ans2

        ans = 0
        mixx = -1
        for i in nums:
            if(i != 0):
                ans += 1
                ans1, ans2 = h2(i)
                ans += ans2
                mixx = max(ans1, mixx)
        ans += mixx
        return int(ans)
