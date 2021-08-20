import bisect


class BIT:

    def __init__(self, node_size):
        self._node = node_size + 1
        self.bit = [0] * self._node

    def add(self, index, add_val):
        while index < self._node:
            self.bit[index] += add_val
            index += index & -index

    def sum(self, index):
        res = 0
        while index > 0:
            res += self.bit[index]
            index -= index & -index
        return res


(n, t) = map(int, input().split())
a = list(map(int, input().split()))
ru = [0] * (n + 1)
ans = 0
for i in range(1, n + 1):
    ru[i] = ru[i - 1] + a[i - 1]
rus = sorted(ru)
bit = BIT(n + 2)
for i in range(n + 1):
    ru[i] = bisect.bisect_left(rus, ru[i])
for i in range(n + 1):
    ind = bisect.bisect_left(rus, rus[ru[i]] - t + 1)
    ans += bit.sum(n + 2) - bit.sum(ind)
    bit.add(ru[i] + 1, 1)
print(ans)
