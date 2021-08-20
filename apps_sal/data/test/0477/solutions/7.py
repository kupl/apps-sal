(n, m, i, j, a, b) = list(map(int, input().split()))


def f(x, y):
    (dx, dy) = (abs(x - i), abs(y - j))
    if dx % a or dy % b:
        return -1
    elif dx // a % 2 != dy // b % 2:
        return -1
    elif dx == 0 and dy == 0:
        return 0
    elif i - a < 1 and i + a > n or (j - b < 1 and j + b > m):
        return -1
    else:
        return max(dx // a, dy // b)


v = -1
for p in ((1, m), (n, 1), (n, m), (1, 1)):
    c = f(*p)
    if c != -1 and (v == -1 or c < v):
        v = c
print(v if v != -1 else 'Poor Inna and pony!')
