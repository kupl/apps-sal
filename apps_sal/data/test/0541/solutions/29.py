n, m = map(int, input().split())

ls = []
for i in range(m):
    x, l = map(int, input().split())
    ls.append([x, l])

ls = sorted(ls, key=lambda x: x[1])
ans = m
for i in range(1, m):
    if ls[i][0] < ls[i - 1][1]:
        ls[i][1] = ls[i - 1][1]
        ans -= 1

print(ans)
