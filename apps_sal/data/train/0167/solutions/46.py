class Solution:
    def superEggDrop1(self, K: int, N: int) -> int: # 超时！！！
        memo = [[2**31-1] * (N+1) for _ in range(K+1)]
        
        def dp(k, n):
            if k == 0: return 0
            if k == 1: return n
            if n <= 1: return n
            
            if memo[k][n] < 2**31-1:
                return memo[k][n]
            
            ans = memo[k][n]
            for i in range(1, n+1):
                ans = min(ans, 1+max(dp(k-1, i-1), dp(k, n-i)))
                # 极小极大过程！！！alike
            memo[k][n] = ans
            return ans
        return dp(K, N)
    
    # D(K-1, i-1), monotonically increasing with i
    # D(K, N-i) is monotonically decreasing with i!
    
    # binary search!
    # D(K, N) = 1 + min(max(D(K-1, i-1), D(K, N-i))), 1<=i<=N
    # f(i) = D(K-1, i-1), f(i) is monotonically increasing with i
    # g(i) = D(K, N-i), g(i) is monotonically decreasing with i
    
    # we can use binary search to find i that minimizes max(f(i), g(i))
    #
    # 一个函数单调增；一个函数单调减
    # min (max (f, g))
    # 就可以使用binary search
    # f(i) < g(i) 的时候，说明i太小了，需要增大i
    # f(i) > g(i) 的时候，说明i太大了，需要减少i
    # 我们需要的是first i, such that f(i) >= g(i)
    # time complexity = O(KNlogN) smaller than O(K*N*N)
    # space is same O(KN)
    
    def superEggDrop(self, K: int, N: int) -> int: # 超时！！！
        memo = [[2**31-1] * (N+1) for _ in range(K+1)]
        
        def dp(k, n):
            if k == 0: return 0
            if k == 1: return n
            if n <= 1: return n
            
            if memo[k][n] < 2**31-1:
                return memo[k][n]
            
            #ans = memo[k][n]
            #for i in range(1, n+1):
            #    ans = min(ans, 1+max(dp(k-1, i-1), dp(k, n-i)))
                # 极小极大过程！！！alike
            left = 1
            right = n + 1
            while left < right:
                mid = left + (right - left) // 2
                if dp(k-1, mid-1) >= dp(k, n-mid):
                    right = mid
                else:
                    left = mid + 1
            
            memo[k][n] = 1 + max(dp(k-1, left-1), dp(k, n-left))
            return memo[k][n]
        return dp(K, N)

