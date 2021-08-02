t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    aa = list(map(int, input().split()))
    if m < n or n == 1 or n == 2:
        print(-1)
    else:
        a = [(aa[i], i) for i in range(n)]
        a = sorted(a)
        ans = sum(aa) * 2
        m -= n
        ans += m * (a[0][0] + a[1][0])
        print(ans)
        for i in range(1, n):
            print(i, i + 1)
        print(n, 1)
        for i in range(m):
            print(a[0][1] + 1, a[1][1] + 1)
