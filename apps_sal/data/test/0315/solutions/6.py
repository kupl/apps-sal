n, k = map(int, input().split())
m = list(map(int, input().split()))
s = [m[i] + m[i + 1] for i in range(n - 1)] + [0]

ans = 0
for i in range(n - 1):
    while s[i] < k:
        s[i] += 1
        s[i + 1] += 1
        m[i + 1] += 1
        ans += 1
print(ans)
print(*m)
