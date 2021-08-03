class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        self.sqnums = [x ** 2 for x in range(1, 317)]
        self.cache = dict((sn, True) for sn in self.sqnums)

        def dp(n):
            if n in self.cache:
                return self.cache[n]

            x = int(sqrt(n))
            while x > 0:
                sn = self.sqnums[x - 1]
                if sn >= n:
                    break

                if not dp(n - sn):
                    self.cache[n] = True
                    return True
                x -= 1

            return False

        return dp(n)
