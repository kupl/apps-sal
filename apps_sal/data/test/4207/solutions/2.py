
from collections import defaultdict


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    e = defaultdict(int)
    cnt = 0

    for i in range(n):
        if a[i] == 0:
            if b[i] == 0:
                cnt += 1
            continue
        if b[i] == 0:
            e[(0, 0)] += 1
            continue
        w = gcd(a[i], b[i])
        wa = a[i] / w
        wb = b[i] / w
        e[(wa, wb)] += 1

    ans = 0
    for i in list(e.values()):
        ans = max(ans, i)

    print(cnt + ans)


def __starting_point():
    main()


__starting_point()
