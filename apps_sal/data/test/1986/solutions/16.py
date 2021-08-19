(n, k) = [int(i) for i in input().split()]
f = [0] * n
t = [0] * n
_max = -3 * 10 ** 9
for i in range(0, n):
    (f[i], t[i]) = [int(i) for i in input().split()]
    _max = max(_max, f[i] - (t[i] - k) if t[i] > k else f[i])
print(_max)
