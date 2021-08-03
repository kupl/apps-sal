n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    q = p[i]
    if p[i] == i + 1:
        p[i] = p[i + 1]
        p[i + 1] = q
        ans += 1
if p[n - 1] == n:
    ans += 1
print(ans)
