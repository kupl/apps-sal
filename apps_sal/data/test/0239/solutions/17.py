from math import hypot
(n, m) = list(map(int, input().split()))
f = False
if n > m:
    (n, m) = (m, n)
    f = True
if n == 0:
    for el in [(0, 1), (0, m), (0, 0), (0, m - 1)]:
        print(*(el if not f else reversed(el)))
else:
    p = [[(0, 0), (n, m), (n, 0), (0, m)], [(1, 0), (n, m), (0, 0), (n - 1, m)]]

    def t(x):
        return sum((hypot(x[i][0] - x[i - 1][0], x[i][1] - x[i - 1][1]) for i in range(1, 4)))
    for el in max(p, key=t):
        print(*(el if not f else reversed(el)))
