__author__ = 'JS'
n = int(input())
k = [0] * 2015
X = [0] * 2015
Y = [0] * 2015
eps = 1e-12
for i in range(n):
    (X[i], Y[i]) = list(map(int, input().split(' ')))
ans = (n - 2) * (n - 1) * n // 6
sum = 0
for i in range(n):
    tot = 0
    cnt = 0
    for j in range(i + 1, n):
        if X[i] != X[j]:
            k[tot] = (Y[j] - Y[i]) / (X[j] - X[i])
            tot += 1
        else:
            cnt += 1
    sum += (cnt - 1) * cnt // 2
    k = sorted(k[:tot]) + k[tot:]
    cnt = 1
    for j in range(1, tot):
        if abs(k[j] - k[j - 1]) < eps:
            cnt += 1
        else:
            sum += (cnt - 1) * cnt // 2
            cnt = 1
    sum += (cnt - 1) * cnt // 2
ans -= sum
print(ans)
