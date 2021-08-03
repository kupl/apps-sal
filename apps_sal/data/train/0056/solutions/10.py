def solve():
    n, m = map(int, input().split())
    ans = 2 if m % n else 0
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        if m <= 0:
            break
        for j in range(n):
            if m <= 0:
                break
            a[j][(i + j) % n] = 1
            m -= 1
    print(ans)
    for i in a:
        print(*i, sep='')


t = int(input())
for _ in range(t):
    solve()
