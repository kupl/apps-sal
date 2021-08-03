class Solution:
    def get_power(self, n):
        res = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            res += 1
        return res

    def getKth(self, lo: int, hi: int, k: int) -> int:
        array = []
        for i in range(lo, hi + 1):
            array.append((i, self.get_power(i)))
        array.sort(key=lambda x: (x[1], x[0]))
        return array[k - 1][0]
