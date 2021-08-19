(n, m) = (int(input()) + 1, 1000001)
(d, s) = (1000000007, 0)
(t, b, c) = ([0] * m, [1] * n, [0] * m)
for i in range(2, n):
    b[i] = b[i - 1] * 2 % d
for i in input().split():
    c[int(i)] += 1
for i in range(m, 1, -1):
    k = sum(c[i::i])
    if k:
        t[i] = (k * b[k] - sum(t[i::i])) % d
        s += i * t[i]
print(s % d)
