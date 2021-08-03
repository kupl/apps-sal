n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    if i + 1 == p[i]:
        p[i], p[i + 1] = p[i + 1], p[i]
        ans += 1
if n == p[-1]:
    ans += 1
print(ans)
