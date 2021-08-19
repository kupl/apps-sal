class Solution:
    dp = {}

    def findPower(self, num):
        way = [num]
        ops = 0
        while num != 1 and num not in self.dp:
            if num % 2 == 0:
                num /= 2
            else:
                num = num * 3 + 1
            way.append(num)
            ops += 1
        if num in self.dp:
            ops += self.dp[num]
        for prev in way:
            self.dp[prev] = ops
            ops -= 1

    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        for i in range(lo, hi + 1):
            self.findPower(i)
            res.append((i, self.dp[i]))
        res = sorted(res, key=lambda x: x[1])
        return res[k - 1][0]
