(a, b, w, x, c) = map(int, input().split())


def result(a, b, w, x, c, s):
    na = a - (s * x - b) / w
    nc = c - s
    return (na, nc)


def solve(a, b, w, x, c):
    left = 0
    right = 1e+16
    if c <= a:
        return 0
    while left < right:
        half = (left + right) // 2
        ret = result(a, b, w, x, c, half)
        if ret[1] <= ret[0]:
            right = half
        else:
            left = half + 1
    return left


print(int(solve(a, b, w, x, c)))
