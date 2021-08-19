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
            normalize[x][y] = nx * 1000 + ny
    tokens = [int(i) for i in sys.stdin.read().split()]
    tokens.reverse()
    n = tokens.pop()
    points = [(tokens.pop(), tokens.pop()) for i in range(n)]
    result = 0
    for i in range(n):
        (x0, y0) = points[i]
        angles = defaultdict(int)
        for j in range(i + 1, n):
            (x, y) = points[j]
            angles[normalize[x - x0][y - y0]] += 1
        for j in list(angles.values()):
            result += j * (n - i - 1 - j)
    print(result // 2)


main()
