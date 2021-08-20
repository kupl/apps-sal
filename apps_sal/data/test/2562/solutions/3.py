(n, m) = (int(input()) + 1, 1000001)
(d, s) = (1000000007, 0)
(t, c) = ([0] * m, [0] * m)
for i in input().split():
    c[int(i)] += 1
for i in range(m, 1, -1):
    k = sum(c[i::i])
    if k:
        t[i] = (k * pow(2, k - 1, d) - sum(t[i::i])) % d
        s += i * t[i]
print(s % d)
