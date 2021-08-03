n, m = [int(x) for x in input().split()]
ans = 0
off = 0


def summ(x):
    return x * (x + 1) // 2


def minn():
    x = n // 2
    left = x
    right = n - x - 1
    return summ(left) + summ(right)


def maxx():
    x = 0
    left = x
    right = n - x - 1
    return summ(left) + summ(right)


for i in range(m):
    a, b = [int(x) for x in input().split()]
    off += a
    if b < 0:
        ans += b * minn()
    else:
        ans += b * maxx()
print(ans / n + off)
