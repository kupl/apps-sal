class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        g = {}
        for i in range(lo, hi + 1):
            p = self.power(i, 0)
            g[i] = p
        s = sorted(list(g.items()), key=lambda x: x[1])
        return(s[k - 1][0])

    def power(self, num, count):
        if num == 1:
            return count
        elif num % 2 == 0:
            return self.power(num // 2, count + 1)
        else:
            return self.power(3 * num + 1, count + 1)
