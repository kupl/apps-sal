import math


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def solve():

    n = int(input())
    ar = list(map(int, input().split()))
    ar = [0, ] + ar
    mark = [0] * (n + 1)

    ans = list()
    for i in range(1, n + 1):

        if mark[i] == 0:
            start = i
            ver = i
            count = 0
            while mark[ver] == 0:
                mark[ver] = 1
                ver = ar[ver]
                count = count + 1
            if ver == start:
                if count % 2 == 0:
                    ans = ans + [count // 2]
                else:
                    ans = ans + [count]
            else:
                print(-1)
                return

    f = 1
    for x in ans:
        f = f * x // gcd(f, x)
    print(f)


solve()
