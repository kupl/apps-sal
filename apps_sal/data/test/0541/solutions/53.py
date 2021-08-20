(N, M) = map(int, input().split())
a = []
for i in range(M):
    (x, y) = map(int, input().split())
    a.append([x, y])
a.sort(key=lambda x: x[1])
ans = 0
for i in range(M - 1):
    if a[i + 1][0] < a[i][1]:
        a[i + 1][1] = a[i][1]
    else:
        ans += 1
ans += 1
print(ans)
