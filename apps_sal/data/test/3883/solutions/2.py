(a, b) = list(map(int, input().split()))


def solve(a, b):
    if a < b:
        return -1
    if b == 0:
        return -1
    if a == b:
        return a
    k0 = (a - b) // (2 * b)
    if k0 == 0:
        x0 = float('inf')
    else:
        x0 = (a - b) / (2 * k0)
    k1 = (a + b) // (2 * b)
    x1 = (a + b) / (2 * k1)
    return min(x0, x1)


print(solve(a, b))
