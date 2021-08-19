class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # Solution 1: DP by myself (9532ms: 5.06%)
        '''
        ele = [item**2 for item in range(1, int(math.sqrt(n))+1)]
        memo = {}
        def helper(amount, person):
            if amount == 0:
                memo[(amount, person)] = False
                return False
            if amount<0:
                return
            if (amount, person) in memo:
                return memo[(amount, person)]
            for item in ele:
                if item<=amount:
                    if not helper(amount-item, -person):
                        memo[(amount, person)] = True
                        return True
                else:
                    break
            memo[(amount, person)] = False
            return False
        return helper(n, 1)
        '''
        # Solution 2: TLE!!
        '''
        dp = [False]*(n+1)
        def check(n):
            if n==0:
                return False
            if n==1:
                dp[1] = True
                return True
            for i in range(int(math.sqrt(n)), 0, -1):
                if not check(n-i*i):
                    dp[n] = True
                    return True
            return False
        return check(n)
        '''
        # Solution 3: DP from discussion (2132ms: 44.64%)
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, int(i**0.5) + 1):
                if not dp[i - j * j]:
                    dp[i] = True
                    break
        return dp[-1]
