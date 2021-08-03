def solve():
    c, m, x = list(map(int, input().split()))
    u = min(c, m)
    y = c - u + m - u + x
    if y >= u:
        print(u)
        return
    print(y + (u - y) * 2 // 3)


t = int(input())

for _ in range(t):
    solve()
