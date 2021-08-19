(n, m) = map(int, input().split())
x = sorted(list(map(int, input().split())))
dif = []
for i in range(m - 1):
    dif.append(x[i + 1] - x[i])
dif = sorted(dif)[::-1]
print(sum(dif[n - 1:]))
