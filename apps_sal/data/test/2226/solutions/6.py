import sys
input = sys.stdin.readline
(n, m, q) = list(map(int, input().split()))
MOD = 10 ** 9 + 7
edges = []
adj = [[] for _ in range(n)]
for i in range(m):
    (a, b, w) = list(map(int, input().split()))
    a -= 1
    b -= 1
    edges.append((a, b, w))
    adj[a].append((b, w))
    adj[b].append((a, w))
INF = 10 ** 18
ans = 0
DP = [-INF] * n
DP[0] = 0
for plen in range(m):
    NDP = [-INF] * n
    for (a, b, w) in edges:
        NDP[b] = max(NDP[b], DP[a] + w)
        NDP[a] = max(NDP[a], DP[b] + w)
    DP = NDP
    ans = (ans + max(DP)) % MOD
' From PyRival '


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

        def intersect(i, j):
            return (M[j] - M[i]) // (K[i] - K[j])
    else:

        def intersect(i, j):
            return (M[j] - M[i]) / (K[i] - K[j])
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
                if hull_x:
                    hull_x.pop()
            else:
                x = intersect(i, hull_i[-1])
                if hull_x and x <= hull_x[-1]:
                    hull_i.pop()
                    hull_x.pop()
                else:
                    hull_i.append(i)
                    hull_x.append(x)
                    break
    return (hull_i, hull_x)


(slope, intersect) = ([], [])
for (a, b, w) in edges:
    i = max(a, b, key=lambda i: DP[i])
    assert DP[i] > 0
    slope.append(w)
    intersect.append(DP[i])
(hull_i, hull_x) = convex_hull_trick(slope, intersect)


def tri(x):
    return x * (x + 1) // 2


lt = 0
for (i, j) in enumerate(hull_i):
    (wt, w) = (intersect[j], slope[j])
    until = min(q if i == len(hull_x) else hull_x[i], q - m)
    if until <= 0:
        continue
    active = until - lt
    ans = (ans + active * wt) % MOD
    min_uses = lt
    max_uses = lt + active
    times = tri(max_uses) - tri(min_uses)
    ans = (ans + times * w) % MOD
    lt = until
    if lt == q - m:
        break
print(ans)
