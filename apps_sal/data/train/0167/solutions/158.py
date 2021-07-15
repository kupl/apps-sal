class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}
        def dp(k, n):
            if (k, n) in memo: return memo[(k, n)]
            if k == 1:
                return n
            if n == 0:
                return 0
            start = 1
            end = n
            res = float('inf')
            while start <= end:
                mid = (start+end)//2
                pre = dp(k-1, mid-1)+1
                cur = dp(k, n-mid)+1
                if pre < cur:
                    res = min(res, cur)
                    start = mid+1
                elif pre > cur:
                    res = min(res, pre)
                    end = mid-1
                else:
                    res = pre
                    break
            memo[(k, n)] = res
            return res
        return dp(K, N)

