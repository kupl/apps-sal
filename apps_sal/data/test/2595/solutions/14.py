import sys


def I():
    return sys.stdin.readline().rstrip()


for tc in range(1, 1 + int(I())):
    (a, b) = list(map(int, I().split()))
    (al, bl) = (0, 0)
    while a > 0 and a % 2 == 0:
        al += 1
        a //= 2
    while b > 0 and b % 2 == 0:
        bl += 1
        b //= 2
    if a == b:
        d = abs(al - bl)
        print((d + 2) // 3)
    else:
        print(-1)
