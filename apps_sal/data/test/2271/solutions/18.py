def computeDegrees(n):
    degrees = [0 for vertex in range(n)]
    for edge in range(n - 1):
        (v1, v2) = list(map(int, input().split()))
        degrees[v1 - 1] += 1
        degrees[v2 - 1] += 1
    return degrees


def computeNumberOfLength2Paths(degrees):
    return int(sum((d * (d - 1) for d in degrees)) / 2)


def __starting_point():
    n = int(input())
    degrees = computeDegrees(n)
    print(computeNumberOfLength2Paths(degrees))


__starting_point()
