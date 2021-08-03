n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    if i + 1 == p[i]:
        tmp = p[i]
        p[i] = p[i + 1]
        p[i + 1] = tmp
        ans += 1

if n == p[n - 1]:
    tmp = p[n - 1]
    p[n - 1] = p[n - 2]
    p[n - 2] = tmp
    ans += 1

print(ans)
