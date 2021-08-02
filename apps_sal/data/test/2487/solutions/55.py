N = int(input())

ans = 0
for i in range(1, N + 1):
    ans += i * (N + 1 - i)

for i in range(N - 1):
    u, v = list(map(int, input().split()))
    u, v = min(u, v), max(u, v)
    ans -= (N - v + 1) * u

print(ans)
