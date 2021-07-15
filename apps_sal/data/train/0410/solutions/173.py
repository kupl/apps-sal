class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = dict()
        dp[0] = dp[2] = 1
        dp[1] = 0
        
        def calc(x):
            if dp.get(x) is not None:
                return dp.get(x)
            if x%2 == 0:
                dp[x] = calc(x//2)+1
            else:
                dp[x] = calc(x*3+1)+1
            return dp[x]
                
        to_sort = []
        for i in range(lo,hi+1):
            calc(i)
            to_sort.append([i, dp.get(i)])
        sorted_res = sorted(to_sort, key=lambda x: x[1])
        return sorted_res[k-1][0]
