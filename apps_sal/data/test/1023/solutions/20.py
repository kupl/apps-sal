import bisect
(n, m, ta, tb, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if n - k <= 0 or m - k <= 0:
    print(-1)
elif n - k == 1 and a[n - 1] + ta > b[m - 1]:
    print(-1)
else:
    d = {}
    for i in range(n):
        j = bisect.bisect_left(b, a[i] + ta)
        d[a[i]] = j
    ma = -1
    flag = 1
    for i in range(k, -1, -1):
        kr = k - i
        if d[a[i]] + kr >= m:
            flag = 0
            break
        if d[a[i]] + kr <= m - 1 and b[d[a[i]] + kr] + tb > ma:
            ma = b[d[a[i]] + kr] + tb
    if flag:
        print(ma)
    else:
        print(-1)
