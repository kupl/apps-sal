n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

dif = []
for i in range(m - 1):
    dif.append(x[i] - x[i + 1])

dif.sort()
ans = abs(sum(dif[n - 1:]))
print(ans)
