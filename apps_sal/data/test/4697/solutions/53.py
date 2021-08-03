n, m = list(map(int, input().split()))

if(2 * n >= m):
    print((m // 2))
else:
    remaining = m - n * 2
    ans = remaining // 4 + n
    print(ans)
