n = int(input())
a = list(map(int, input().split()))
ans = a[0]
l = []

for i in range(1, n, 2):
    ans -= a[i]
    ans += a[i + 1]

l.append(ans)

for i in range(n - 1):
    ans = a[i] * 2 - ans
    l.append(ans)

print(*l)
