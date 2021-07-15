class Solution:
    def num_count(self, x, count):
        if x == 1:
            return count
        count += 1
        if x % 2 == 0:
            x = x // 2
        else:
            x = x * 3 + 1
        if x in self.dp:
            return count + self.dp[x]
        return self.num_count(x, count)
        
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.dp = {}
        for x in range(lo, hi + 1):
            self.dp[x] = self.num_count(x, 0)
        return sorted(self.dp.items(), key = lambda x : x[1])[k - 1][0]
