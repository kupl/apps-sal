def solve():
    n, m, x, y = map(int, input().split())
    y = min(y, x * 2)
    a = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        j = 0
        while j < m:
            if a[i][j] == '*':
                j += 1
                continue
            k = j
            while k < m and a[i][k] == '.':
                k += 1
            w = k - j
            ans += w // 2 * y + w % 2 * x
            j = k
    print(ans)

t = int(input())
for _ in range(t):
    solve()
