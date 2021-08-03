def bf(n, m, a):
    k = 0
    for c in range(1, n + 1):
        if abs(c - a) < abs(c - m):
            k += 1
    return k


def solve(n, m):
    maxx = 0
    for i in range(1, n + 1):
        maxx = max(maxx, bf(n, m, i))
    for i in range(1, n + 1):
        if bf(n, m, i) == maxx:
            return(i)


def solve2(a, b):
    if a == 1 and b == 1:
        return 1
    if a == b:
        return a - 1
    if b >= a:
        return max(a - (b - a) + 1, 1)
    k = b - 1
    l = b + 1
    c1 = a - l + 1
    if k >= c1:
        return k
    else:
        return l


a, b = list(map(int, input().split(' ')))
print(solve2(a, b))
