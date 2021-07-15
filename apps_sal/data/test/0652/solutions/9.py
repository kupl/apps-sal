def middle(a, b):
    return (b[0] + a[0])/2, (b[1] + a[1])/2


def solve(n, points):
    middles = dict()
    solutions = 0
    for i in range(n-1):
        for j in range(i+1, n):

            s = middle(points[i], points[j])
            solutions += middles.setdefault(s, 0)
            middles[s] += 1

    return solutions


def __starting_point():
    n = int(input())
    points = list()
    for _ in range(n):
        points.append(tuple(map(int, input().split())))

    print(solve(n, points))









__starting_point()
