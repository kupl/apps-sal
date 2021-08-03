import sys


def I():
    return sys.stdin.readline().rstrip()


for _ in range(int(I())):
    n = int(I())
    a = [0, 1]
    i = n
    while i > 0:
        if n // i > a[-1]:
            a.append(n // i)
        i = n // (a[-1] + 1)
    print(len(a))
    print(*a)
