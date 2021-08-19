MAXN = 200001
(n, m) = list(map(int, input().split(' ')))
s = list(map(int, input().split(' ')))
f = [0 for i in range(n + 1)]
count = [0 for i in range(-MAXN, MAXN + 1)]
f[0] = 0
last = 0
res = 0
for i in range(1, n + 1):
    if s[i - 1] == m:
        for j in range(last, i):
            count[f[j]] += 1
        last = i
    if s[i - 1] > m:
        f[i] = f[i - 1] - 1
    else:
        f[i] = f[i - 1] + 1
    res += count[f[i]] + count[f[i] - 1]
print(res)
