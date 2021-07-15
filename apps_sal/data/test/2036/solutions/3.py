mod = 10**9 + 7
def solve():
    n, m, x, y = map(int, input().split())
    for i in range(n):
        for j in range(m):
            print(x, y)
            if j + 1 == m:
                continue
            y = y + 1
            if y > m:
                y = 1
        x = x + 1
        if x > n:
            x = 1
t = 1
for _ in range(t):
    solve()
