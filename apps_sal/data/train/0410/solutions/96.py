class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def helper(num):
            if(num == 1):
                return 0
            # if dp[num] != -1:
            #     return dp[num]
            if num%2 == 0:
                return helper(num//2) + 1
            else:
                return helper((num*3)+1) + 1
            # return dp[num]
         
        # dp = [-1 for i in range(1000000)]
        # dp[1] = 0
        res = []
        for i in range(lo, hi+1):
            res.append((helper(i), i))
        res.sort()
        return res[k-1][1]

