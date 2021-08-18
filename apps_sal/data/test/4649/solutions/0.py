import sys


def countR(ip):
    c = 0
    for i in ip:
        if(i == 'R'):
            c += 1
    return c


def countB(ip):
    c = 0
    for i in ip:
        if(i == 'B'):
            c += 1
    return c


def countG(ip):
    c = 0
    for i in ip:
        if(i == 'G'):
            c += 1
    return c


t = int(sys.stdin.readline())
x = 'RGB' * 680
y = 'GBR' * 680
z = 'BRG' * 680
for i in range(t):
    n, k = list(map(int, sys.stdin.readline().strip().split()))
    a = sys.stdin.readline().strip()
    xk = x[:k]
    yk = y[:k]
    zk = z[:k]

    op = 2001
    for j in range(n - k + 1):
        b = a[j:j + k]

        xd = 0
        yd = 0
        zd = 0
        for jj in range(len(b)):
            if(b[jj] != xk[jj]):
                xd += 1
            if(b[jj] != yk[jj]):
                yd += 1
            if(b[jj] != zk[jj]):
                zd += 1
        op = min(op, xd, yd, zd)
    print(op)
