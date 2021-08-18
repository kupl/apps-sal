
t = 1
for test in range(1, t + 1):
    n, m = list(map(int, input().split()))
    a = 0
    b = 0
    c = []
    for i in range(n):
        l, r = list(map(int, input().split()))
        a += l
        b += r
        c.append(l - r)
    if b > m:
        print(-1)
    else:
        c.sort(reverse=True)
        diff = a - m
        ans = 0
        ind = 0
        while diff > 0:
            diff -= c[ind]
            ind += 1
            ans += 1
        print(ans)
