import math
MOD = 10 ** 9 + 7


def dist(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx * dx + dy * dy)


def max_dist(p, x, y):
    result = 0
    for i in range(len(p)):
        result = max(result, dist((x, y), p[i]))
    return result


def ternary_search2(p, x):
    l = 0
    r = 1000
    for i in range(100):
        c1 = (l * 2 + r) / 3
        c2 = (l + r * 2) / 3
        if max_dist(p, x, c1) > max_dist(p, x, c2):
            l = c1
        else:
            r = c2
    return max_dist(p, x, l)


def ternary_search1(p):
    l = 0
    r = 1000
    for i in range(100):
        c1 = (l * 2 + r) / 3
        c2 = (l + r * 2) / 3
        if ternary_search2(p, c1) > ternary_search2(p, c2):
            l = c1
        else:
            r = c2
    return ternary_search2(p, l)


def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    print(ternary_search1(p))


main()
