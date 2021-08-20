N = int(input())
ans = 0
for v in range(1, N + 1):
    ans += v * (N - v + 1)
for _ in range(N - 1):
    (u, v) = map(int, input().split())
    (u, v) = (min(u, v), max(u, v))
    ans -= u * (N - v + 1)
print(ans)
