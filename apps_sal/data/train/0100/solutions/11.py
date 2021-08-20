def solve():
    (r, g, b) = map(int, input().split())
    (a, b, c) = sorted([r, g, b])
    if a + b <= c:
        ans = a + b
    else:
        ans = a + b + c
        ans //= 2
    print(ans)


t = int(input())
for i in range(t):
    solve()
