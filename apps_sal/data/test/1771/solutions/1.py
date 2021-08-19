import math


def bin_search(a, left, right, threshold):
    left -= 1
    while right - left - 1 > 0:
        m = int((left + right) / 2)
        if a[m] < threshold:
            left = m
        else:
            right = m
    return right


def divide(a, b):
    if b == 0:
        if a > 0:
            return math.inf
        else:
            return -math.inf
    return a / b


def main():
    (n, l, w) = [int(x) for x in input().split()]
    (u, v) = ([], [])
    for i in range(n):
        (x, vel) = [int(x) for x in input().split()]
        if vel > 0:
            u.append(x)
        else:
            v.append(x)
    u = sorted(u)
    v = sorted(v)
    ans = 0
    for x in v:
        threshold = min(divide((x + l) * (w + 1), w - 1), -(x + l), x)
        r1 = bin_search(u, 0, len(u), threshold)
        threshold = min(divide((x + l) * (w - 1), w + 1), x)
        r2 = bin_search(u, 0, len(u), threshold)
        l2 = bin_search(u, 0, len(u), -(x + l))
        if l2 <= r1:
            ans += r2
        else:
            ans += r1
            ans += max(0, r2 - l2)
    print(ans)


def __starting_point():
    main()


__starting_point()
