n = int(input())
p = list(map(int, input().split()))
for i in range(n):
    p[i] -= 1
ans = 0
for i in range(n - 1):
    if p[i] == i:
        ans += 1
        (p[i], p[i + 1]) = (p[i + 1], p[i])
if p[n - 1] == n - 1:
    ans += 1
print(ans)
