N = int(input())
UV = [list(map(int, input().split())) for _ in range(N - 1)]
ans = 0
for i in range(N):
    ans += (i + 1) * (N - i)
for u, v in UV:
    if u > v:
        u, v = v, u
    ans -= u * (N - v + 1)
print(ans)
