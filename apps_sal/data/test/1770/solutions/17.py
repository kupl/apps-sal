import math
n = int(input())


def f(x, y, d):
    t = abs(x - y)
    if y == 1:
        return math.ceil(t / d)
    if y == n:
        return math.ceil(t / d)
    if t % d == 0:
        return t // d
    else:
        return 2 * (10**9)


for i in range(n):
    n, x, y, d = list(map(int, input().split()))
    ans = min([f(x, y, d), f(x, 1, d) + f(1, y, d), f(x, n, d) + f(n, y, d)])
    if ans == 2 * (10**9):
        print("-1")
    else:
        print(ans)
