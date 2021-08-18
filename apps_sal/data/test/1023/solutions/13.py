INF = 100_000_000


t = 1

for test in range(t):
    n, m, ta, tb, k = (((list(map(int, input().split())))))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        a[i] = a[i] + ta

    ans = 0
    ind = 0
    if k >= n or k >= m:
        print(-1)
        continue
    for i in range(k + 1):
        lo = a[i]
        while ind < m and b[ind] < lo:
            ind += 1
        if ind == m:
            ans = -1
            break
        else:
            if ind + k - i >= m:
                ans = -1
                break
            ans = max(ans, b[ind + (k - i)] + tb)
    print(ans)
