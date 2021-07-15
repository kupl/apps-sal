n = int(input())
_l = list(map(int, input().split()))
l = [abs(_l[i] - _l[i + 1]) for i in range(n - 1)]
p, n, res = 0, 0, 0
for e in l:
    _p = max(0, n + e)
    _n = max(0, p - e)
    p, n = _p, _n
    res = max(p, n, res)
print(res)
