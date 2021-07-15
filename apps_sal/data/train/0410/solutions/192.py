class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = {}
        dp[1] = 0
        def helper(num):
            if num in dp:
                return dp[num]
            if num == 1:
                return 0
            if num%2 == 0:
                dp[num] = helper(num//2) + 1
            else:
                dp[num] = helper((num*3)+1) + 1
            print((dp[num]))
            return dp[num]
        res = []
        for i in range(lo, hi+1):
            res.append((helper(i), i))
        res.sort()
        return res[k-1][1]

