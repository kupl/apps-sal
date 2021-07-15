def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        ans += max(a[i - 1] - a[i], 0)
    print(ans)

t = int(input())
for _ in range(t):
    solve()
