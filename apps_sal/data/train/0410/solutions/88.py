class Solution:
    def get_power(self, n):
        if n == 1:
            return 0
        elif n % 2 == 0:
            return 1 + self.get_power(n // 2)
        else:
            return 1 + self.get_power(3 * n + 1)

    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums = [i for i in range(lo, hi + 1)]

        lst2 = []
        for num in nums:
            lst2.append((num, self.get_power(num)))

        lst2.sort(key=lambda x: x[1])

        return lst2[k - 1][0]
