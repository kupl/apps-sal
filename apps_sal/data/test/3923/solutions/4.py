# This code sucks, you know it and I know it.
# Move on and call me an idiot later.

def solve(a, b, n):

    i = 0
    while i * a <= n:

        if (n - (i * a)) % b == 0:
            x = i
            y = (n - (i * a)) // b
            return (x, y)
        i = i + 1

    return (-1, -1)


n, a, b = map(int, input().split())
aa, bb = solve(a, b, n)
l = []
if (aa, bb) == (-1, -1):
    print(-1)
else:

    for i in range(1, aa + 1):
        x = a * (i - 1) + 1
        y = a * i
        l += [y]
        l += [j for j in range(x, y)]

    for i in range(1, bb + 1):
        x = a * aa + b * (i - 1) + 1
        y = a * aa + b * i
        l += [y]
        l += [j for j in range(x, y)]

    print(" ".join(map(str, l)))
