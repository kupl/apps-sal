class Solution:

    def getPower(self, n):
        if n == 1:
            return 0
        if n in self.dp:
            return self.dp[n]
        elif n % 2 == 0:
            self.dp[n] = self.getPower(n // 2) + 1
        else:
            self.dp[n] = self.getPower(3 * n + 1) + 1
        return self.dp[n]

    def getKth(self, lo: int, hi: int, k: int) -> int:
        tmp = []
        self.dp = {}
        for num in range(lo, hi + 1):
            tmp.append((num, self.getPower(num)))
        tmp.sort(key=lambda x: (x[1], x[0]))
        return tmp[k - 1][0]
