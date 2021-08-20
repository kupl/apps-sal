class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        return self.dfs(n)

    @lru_cache(None)
    def dfs(self, remain):
        sqrt_root = int(math.sqrt(remain))
        for i in range(1, sqrt_root + 1):
            if not self.dfs(remain - i * i):
                return True
        return False
    '\n        return self.helper(n, True)\n    \n    def helper(self, n, label):\n        value = math.sqrt(n)\n        if value == int(value):\n            return label\n        re = False\n        \n        for i in range(n,0, -1):\n            ii = math.sqrt(i)\n            if ii == int(ii):\n                print(ii, label)\n                re = self.helper(n-int(ii*ii), not label)\n        return re \n    '
