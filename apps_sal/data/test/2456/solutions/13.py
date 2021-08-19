def solve():
    ans = 0
    (n, k) = map(int, input().split())
    u = min(k, n - 1)
    ans += (1 + u) * u // 2
    if k > n - 1:
        ans += 1
    print(ans)


t = int(input())
for _ in range(t):
    solve()
