import sys


def I():
    return sys.stdin.readline().rstrip()


for _ in range(int(I())):
    (n, m) = list(map(int, I().split()))
    a = list(map(int, I().split()))
    if n > m or n == 2:
        print(-1)
    else:
        s = 2 * sum(a)
        b = sorted(a)
        i = a.index(b[0])
        a[i] = 100000.0
        j = a.index(b[1])
        m -= n
        s += sum(b[:2]) * m
        print(s)
        for k in range(n):
            print(k + 1, (k + 1) % n + 1)
        for k in range(m):
            print(i + 1, j + 1)
