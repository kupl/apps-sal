class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        """
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
        """
        '\n        dp = [False]*(n+1)\n        def check(n):\n            if n==0:\n                return False\n            if n==1:\n                dp[1] = True\n                return True\n            for i in range(int(math.sqrt(n)), 0, -1):\n                if not check(n-i*i):\n                    dp[n] = True\n                    return True\n            return False\n        return check(n)\n        '
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                if not dp[i - j * j]:
                    dp[i] = True
                    break
        return dp[-1]
