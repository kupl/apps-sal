def ii():
    return int(input())


def ss():
    return [x for x in input()]


def si():
    return [int(x) for x in input().split()]


def mi():
    return map(int, input().split())


def r(s):
    return s[0] - s[1]


t = ii()
for i in range(t):
    (a, b) = mi()
    s = [si() for i in range(a)]
    maxout = max(s, key=lambda x: x[0])[0]
    maxin = max(s, key=lambda x: x[0] - x[1])
    maxin = maxin[0] - maxin[1]
    if b <= maxout:
        print(1)
    elif maxin <= 0:
        print(-1)
    else:
        print((b - maxout - 1) // maxin + 2)
