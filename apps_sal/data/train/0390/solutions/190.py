class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        memo = {0: False}

        def wing(x):
            if math.sqrt(x) == int(math.sqrt(x)):
                return True
            if x in memo:
                return memo[x]
            i = 1
            ans = False
            while i * i <= x:
                if wing(x - i * i) == False:
                    ans = True
                    break
                i += 1
            memo[x] = ans
            return ans
        return wing(n)
