def main():
    import sys
    from collections import defaultdict
    from fractions import gcd
    precalc_gcd = [[gcd(i, j) for j in range(201)] for i in range(201)]
    tokens = [int(i) for i in sys.stdin.read().split()]
    tokens.reverse()
    n = tokens.pop()
    points = [(tokens.pop(), tokens.pop()) for i in range(n)]
    result = 0
    for (x0, y0) in points:
        angles = defaultdict(int)
        for (x, y) in points:
            if x == x0 and y == y0:
                continue
            x -= x0
            y -= y0
            if x < 0 or (x == 0 and y < 0):
                x = -x
                y = -y
            g = precalc_gcd[abs(x)][abs(y)]
            x //= g
            y //= g
            angles[x * 1000 + y] += 1
        for i in list(angles.keys()):
            result += angles[i] * (n - 1 - angles[i])
    print(result // 6)


main()
