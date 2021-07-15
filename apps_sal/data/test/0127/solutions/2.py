n, f = list(map(int, input().split()))
d = []
for i in range(n):
    d.append(list(map(int, input().split())))
d.sort(reverse=True, key=lambda x: min(2 * x[0], x[1]) - min(x[0], x[1]))
res = 0
for i in range(n):
    if i < f:
        res += min(2 * d[i][0], d[i][1])
    else:
        res += min(d[i][0], d[i][1])
print(res)

