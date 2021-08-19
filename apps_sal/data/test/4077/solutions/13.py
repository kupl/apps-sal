class BIT():
    def __init__(self, n):
        self.BIT = [0] * (n + 1)
        self.num = n

    def query(self, idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx & (-idx)
        return res_sum

    # Ai += x O(logN)
    def update(self, idx, x):
        while idx <= self.num:
            self.BIT[idx] += x
            idx += idx & (-idx)
        return


n, m = map(int, input().split())
a = list(map(int, input().split()))


def solve(x):
    tmp = [0 for i in range(n)]
    for i in range(n):
        if a[i] > x:
            tmp[i] = -1
        else:
            tmp[i] = 1
        tmp[i] += tmp[i - 1]

    tmp = [0] + tmp
    val = list(set([tmp[j] for j in range(n + 1)]))
    val.sort()
    comp = {i: e + 1 for e, i in enumerate(val)}

    bit = BIT(n + 1)
    res = 0
    for i in range(n + 1):
        res += bit.query(comp[tmp[i]])
        bit.update(comp[tmp[i]], 1)
    return res


print(solve(m) - solve(m - 1))
