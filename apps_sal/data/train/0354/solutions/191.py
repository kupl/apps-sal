class Solution:

    def __init__(self):
        self.store = defaultdict(int)

    def rds(self, n, rm, pre, prec):
        if n == 0:
            return 1
        elif (n, pre, prec) in self.store:
            return self.store[n, pre, prec]
        else:
            result = 0
            for i in range(6):
                if i == pre:
                    if prec < rm[i]:
                        result += self.rds(n - 1, rm, i, prec + 1)
                else:
                    result += self.rds(n - 1, rm, i, 1)
            result %= 1000000007
            self.store[n, pre, prec] = result
            return result

    def dieSimulator(self, n: int, rm: List[int]) -> int:
        res = self.rds(n, rm, None, 0)
        return res
