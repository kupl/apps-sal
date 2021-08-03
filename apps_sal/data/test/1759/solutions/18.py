def R(): return map(int, input().split())


m, n = R()
t = [list([0] * (m + 1)) for i in range(n + 1)]
for i in range(1, m + 1):
    a = list(R())
    for j in range(1, n + 1):
        t[j][i] = max(t[j - 1][i], t[j][i - 1]) + a[j - 1]
print(" ".join(map(str, t[n][1:])))
