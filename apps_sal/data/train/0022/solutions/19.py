t = int(input())
for ii in range(t):
    (a, k) = map(int, input().split())
    cur = 0
    while cur < k - 1 and '0' not in str(a):
        mi = 1000
        ma = -1
        for i in str(a):
            mi = min(int(i), mi)
            ma = max(int(i), ma)
        a += mi * ma
        cur += 1
    print(a)
