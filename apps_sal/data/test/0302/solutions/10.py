class OneArithmetic():
    def __init__(self, n):
        self.n = n
        self.m = [0] * 17
        v = 0
        for i in range(1, 17):
            v = 10 * v + 1
            self.m[i] = v

    def dfs(self, v, d):
        v = abs(v)
        if d == 1:
            return v
        elif v == 0:
            return 0
        else:
            k = int(v / self.m[d])
            ans = min(self.dfs(v - k * self.m[d], d - 1) + k * d, self.dfs((k + 1) * self.m[d] - v, d - 1) + (k + 1) * d)
            return ans

    def min_digits(self):
        v = self.dfs(self.n, 16)
        return v


n = int(input())
print(OneArithmetic(n).min_digits())
