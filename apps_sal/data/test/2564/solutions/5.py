import sys


def inputr():
    return sys.stdin.readline().rstrip('\n')


input = sys.stdin.readline
INF = 10 ** 18
for _ in range(int(input())):
    (a, b, n) = list(map(int, input().split()))
    r = 0
    while a <= n and b <= n:
        r += 1
        if a > b:
            b += a
        else:
            a += b
    print(r)
