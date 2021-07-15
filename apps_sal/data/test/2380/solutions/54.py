n, m = map(int, input().split())
a = list(map(int, input().split()))
bc = []
for _ in range(m):
    b, c = map(int, input().split())
    bc.append([c, b])
a.sort()
bc.sort(reverse = True)
x = [0] * n
i, j = 0, 0
while i < n:
    for _ in range(bc[j][1]):
        x[i] = bc[j][0]
        i += 1
        if i == n:
            break
    j += 1
    if j == m:
        break
ans = 0
for i in range(n):
    ans += max(a[i], x[i])
print(ans)
