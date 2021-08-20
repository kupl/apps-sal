import sys
T = int(sys.stdin.readline().strip())
for t in range(T):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    a.sort()
    m = -1
    mc = 0
    c = 1
    for i in range(1, n):
        if a[i] == a[i - 1]:
            c = c + 1
        else:
            if c > m:
                m = c
                mc = 1
            elif c == m:
                mc = mc + 1
            c = 1
    if c > m:
        m = c
        mc = 1
    elif c == m:
        mc = mc + 1
    print((n - m * mc) // (m - 1) + mc - 1)
