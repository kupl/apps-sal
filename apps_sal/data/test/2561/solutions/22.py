import sys


def minp():
    return sys.stdin.readline().strip()


t = int(minp())
for i in range(t):
    a = int(minp())
    c = 0
    while a > 0:
        if a & 1 != 0:
            c += 1
        a >>= 1
    print(2**c)
