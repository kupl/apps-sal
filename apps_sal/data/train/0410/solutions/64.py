class Solution:
    def getSteps(self, x):
        res = 0
        while x != 1:
            if x % 2 == 1:
                x = 3 * x + 1
            else:
                x = x / 2
            res += 1
        return res

    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        for i in range(lo, hi + 1, 1):
            val = self.getSteps(i)
            res.append([i, val])

        print(res)
        res.sort(key=lambda x: (x[1], x[0]))
        ans = [item[0] for item in res]
        print(ans)
        return ans[k - 1]
