import sys


def I():
    return sys.stdin.readline().rstrip()


for tc in range(1, 1 + int(I())):
    n = int(I())
    ans = 0
    while n:
        ans += n
        n //= 2
    print(ans)
