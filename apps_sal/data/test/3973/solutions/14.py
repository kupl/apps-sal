# Binary Indexed Tree (Fenwick Tree)
class BIT():
    """区間加算、一点取得クエリをそれぞれO(logN)で答える
    add: 区間[l, r)にvalを加える
    get_val: i番目の値を求める
    i, l, rは0-indexed
    """
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def _add(self, i, val):
        while i > 0:
            self.bit[i] += val
            i -= i & -i

    def get_val(self, i):
        """i番目の値を求める"""
        i = i + 1
        s = 0
        while i <= self.n:
            s += self.bit[i]
            i += i & -i
        return s

    def add(self, l, r, val):
        """区間[l, r)にvalを加える"""
        self._add(r, val)
        self._add(l, -val)



n, m = map(int, input().split())
a = list(map(int, input().split()))

bit = BIT(2 * m + 10)
cnt = 0
for i in range(n - 1):
    l, r = a[i], a[i + 1]
    if l > r:
        r += m
    cnt += r - l
    if l == r or l + 1 == r:
        continue
    if l < r:
        l += 2
        r += 1
        bit.add(l, r, 1)
        bit.add(r, r + 1, -(r - l))
        continue

imos = [0] * (2 * m + 2)
for i in range(2 * m + 2):
    imos[i] += bit.get_val(i)
    if i - 1 >= 0:
        imos[i] += imos[i - 1]

ans = [0] * (m + 1)
for i in range(1, m + 1):
    ans[i] = imos[i] + imos[i + m]
print(cnt - max(ans))
