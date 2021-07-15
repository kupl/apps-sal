def getIntersect(a, b, c, d):
    return (max(a, c), min(b, d))


def solve(N, M, A):
    tHi = M
    tLo = M
    A.sort()
    lastT = 0
    for t, l, h in A:
        deltaT = t - lastT
        tLo -= deltaT
        tHi += deltaT
        tLo, tHi = getIntersect(tLo, tHi, l, h)
        if tLo > tHi:
            return "NO"
        lastT = t
    return "YES"


def __starting_point():
    T, = list(map(int, input().split()))
    for t in range(T):
        N, M = list(map(int, input().split()))
        A = []
        for i in range(N):
            tlh = [int(x) for x in input().split()]
            A.append(tlh)

        ans = solve(N, M, A)
        print(ans)

__starting_point()
