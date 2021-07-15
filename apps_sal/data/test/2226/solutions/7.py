import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


MOD = 10 ** 9 + 7
INF = 100


def convex_hull_trick(K, M, integer=True):
    """
    Given lines on the form y = K[i] * x + M[i] this function returns intervals,
    such that on each interval the convex hull is made up of a single line.
    Input:
        K: list of the slopes
        M: list of the constants (value at x = 0)
        interger: boolean for turning on / off integer mode. Integer mode is exact, it
                  works by effectively flooring the seperators of the intervals.
    Return:
        hull_i: on interval j, line i = hull_i[j] is >= all other lines
        hull_x: interval j and j + 1 is separated by x = hull_x[j], (hull_x[j] is the last x in interval j)
    """
    if integer:
        intersect = lambda i, j: (M[j] - M[i]) // (K[i] - K[j])
    else:
        intersect = lambda i, j: (M[j] - M[i]) / (K[i] - K[j])

    assert len(K) == len(M)

    hull_i = []
    hull_x = []
    order = sorted(list(range(len(K))), key=K.__getitem__)
    for i in order:
        while True:
            if not hull_i:
                hull_i.append(i)
                break
            elif K[hull_i[-1]] == K[i]:
                if M[hull_i[-1]] >= M[i]:
                    break
                hull_i.pop()
                if hull_x: hull_x.pop()
            else:
                x = intersect(i, hull_i[-1])
                if hull_x and x <= hull_x[-1]:
                    hull_i.pop()
                    hull_x.pop()
                else:
                    hull_i.append(i)
                    hull_x.append(x)
                    break
    return hull_i, hull_x


def nn2(n):
    return n * (n+1) // 2


def solve(n, m, q, edges):
    # k < m
    # dp[v][k] - max path cost ending in v and having k edges
    dp = [[-INF]*(m+1) for _ in range(n)]
    mk = [0]*(m+1)

    dp[0][0] = 0

    for k in range(1, m+1):
        for e in edges:
            if dp[e[0]][k-1] == -INF:
                continue
            dp[e[1]][k] = max(dp[e[1]][k], dp[e[0]][k-1] + e[2])
            mk[k] = max(mk[k], dp[e[1]][k])

    ans = sum(mk) % MOD
    if q > m:
        intersect = [dp[i][m] for i in range(n)]
        slope = [0] * n

        for e in edges:
            if e[2] > slope[e[0]]:
                slope[e[0]] = e[2]

        hull_i, hull_x = convex_hull_trick(slope, intersect)

        lt = 0
        for i, j in enumerate(hull_i):
            wt = intersect[j]
            w = slope[j]

            until = min(q if i == len(hull_x) else hull_x[i], q - m)
            if until <= 0:
                continue

            active = (until - lt)

            ans = (ans + active * wt) % MOD

            min_uses = lt
            max_uses = lt + active

            times = nn2(max_uses) - nn2(min_uses)
            ans = (ans + times * w) % MOD

            lt = until
            if lt == q - m: break


    return ans

def main():
    n, m, q = ria()
    e = []
    for _ in range(m):
        u, v, w = ria()
        u -= 1
        v -= 1
        e.append((u, v, w))
        e.append((v, u, w))
    wi(solve(n, m, q, e))


def __starting_point():
    main()

__starting_point()
