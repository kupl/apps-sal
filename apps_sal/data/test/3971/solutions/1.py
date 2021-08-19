import sys
3


def compress(l):
    x = l[0]
    cnt = 1
    c = []
    for i in range(1, len(l)):
        if l[i] == x:
            cnt += 1
        else:
            c.append((x, cnt))
            x = l[i]
            cnt = 1
    c.append((x, cnt))
    return c


def __starting_point():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    a.sort()
    a = compress(a)
    dp = [0, a[0][0] * a[0][1]]
    for i in range(1, len(a)):
        (x, c) = a[i]
        px = a[i - 1][0]
        dp.append(max(dp[-1], x * c + (dp[-1] if x > px + 1 else dp[-2])))
    print(max(dp))


__starting_point()
