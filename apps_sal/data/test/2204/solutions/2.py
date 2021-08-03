import sys
input = sys.stdin.readline
for f in range(int(input())):
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    acop = [0] * m
    bcop = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
        acop[i] = a[i]
        bcop[i] = [b[i], i]
    acop.sort(reverse=True)
    bcop.sort(reverse=True)
    mx = 0
    i = 0
    su = 0
    for j in range(m):
        bi = bcop[j][0]
        ii = bcop[j][1]
        ai = a[ii]
        while i < m and acop[i] > bi:
            su += acop[i]
            i += 1
        maxi = ai
        if i < n:
            maxi += su
            if i + 1 < n:
                maxi += (n - i - 1) * bi
            if ai > bi:
                maxi += bi
                maxi -= ai
            mx = max(maxi, mx)
    if n <= m:
        sun = 0
        for i in range(n):
            sun += acop[i]
        mx = max(mx, sun)
    print(mx)
    blank = input()
