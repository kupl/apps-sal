def I(): return map(int, input().split())


R = range
n, m = I()
t = [[]for _ in R(m)]
e = list(R(1, m + 1))
r = 'NO'
for _ in R(n):
    for i, v in zip(R(m), I()):
        t[i] += [v]
for i in R(m):
    for j in R(i, m):
        t[i], t[j] = t[j], t[i]
        if all(3 > sum(t[i][j] != e[i]for i in R(m))for j in R(n)):
            r = 'YES'
        t[i], t[j] = t[j], t[i]
print(r)
