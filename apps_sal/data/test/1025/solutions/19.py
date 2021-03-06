def main():
    import sys
    from collections import defaultdict
    from fractions import gcd
    normalize = [[0] * 405 for i in range(405)]
    for x in range(-200, 201):
        for y in range(-200, 201):
            if x == 0 and y == 0:
                continue
            (nx, ny) = (x, y)
            g = abs(gcd(x, y))
            nx //= g
            ny //= g
            if nx < 0 or (nx == 0 and ny < 0):
                nx = -nx
                ny = -ny
            nx += 200
            ny += 200
            normalize[x][y] = nx * 401 + ny
    tokens = [int(i) for i in sys.stdin.read().split()]
    tokens.reverse()
    n = tokens.pop()
    X = [0] * n
    Y = [0] * n
    for i in range(n):
        (X[i], Y[i]) = (tokens.pop(), tokens.pop())
    result = n * (n - 1) * (n - 2) // 6
    angles = [0] * 170000
    for i in range(n):
        (x0, y0) = (X[i], Y[i])
        for j in range(i + 1, n):
            v = normalize[X[j] - x0][Y[j] - y0]
            result -= angles[v]
            angles[v] += 1
        for j in range(i + 1, n):
            angles[normalize[X[j] - x0][Y[j] - y0]] = 0
    print(result)


main()
