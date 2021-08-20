def solve():
    (n, g, b) = [int(x) for x in input().split()]
    l = 0
    r = int(1e+30)
    while r - l > 1:
        m = (l + r) // 2
        blk = m // (g + b)
        cnt = blk * g + min(g, m % (g + b))
        if cnt >= (n + 1) // 2:
            r = m
        else:
            l = m
    print(max(r, n))


t = int(input())
for _ in range(t):
    solve()
