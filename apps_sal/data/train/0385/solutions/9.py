class Solution:

    def kthFactor(self, n: int, k: int) -> int:
        try:
            return list(filter(lambda x: n % x == 0, range(1, n + 1)))[k - 1]
        except:
            return -1
