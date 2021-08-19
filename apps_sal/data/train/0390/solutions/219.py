class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        def dfs(n):
            if n == 0:
                return False
            if int(n ** 0.5) ** 2 == n:
                return True
            if n not in dic:
                dic[n] = any((not dfs(n - i) for i in poss if i <= n))
            return dic[n]
        poss = []
        dic = {}
        for i in range(1, int(n ** 0.5) + 1):
            poss.append(i * i)
        poss = poss[::-1]
        return dfs(n)
