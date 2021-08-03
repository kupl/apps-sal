class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        self.inc = {1: 0}
        while lo <= hi:
            heapq.heappush(res, (self.find_power(lo), lo))
            lo += 1
        for i in range(k):
            ans = heapq.heappop(res)[1]
        return ans

    def find_power(self, var):
        if var in self.inc:
            return self.inc[var]
        if var % 2 == 0:
            self.inc[var] = self.find_power(var // 2) + 1
        else:
            self.inc[var] = self.find_power(3 * var + 1) + 1
        return self.inc[var]
