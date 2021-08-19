n = int(input())
a = []
for i in range(100):
    a.append([0 for j in range(100)])
for ii in range(n):
    (y1, x1, y2, x2) = list(map(int, input().split()))
    for i in range(y1 - 1, y2):
        for j in range(x1 - 1, x2):
            a[i][j] += 1
ans = 0
for ii in a:
    ans += sum(ii)
print(ans)
