(n, m) = map(int, input().split())
ans = 0
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(0, 2 * m, 2):
        if row[j] + row[j + 1] > 0:
            ans += 1
print(ans)
