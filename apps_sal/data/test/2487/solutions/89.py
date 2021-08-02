n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * (n - i + 1)

for _ in range(n - 1):
    u, v = [int(x) - 1 for x in input().split()]
    if u > v: u, v = v, u
    ans -= (u + 1) * (n - v)

print(ans)
