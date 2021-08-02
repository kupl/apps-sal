from math import *
eps = 1e-9
ans = dict()
ans[(0, 0, 0)] = 4
ans[(0, 0, 1)] = 4
ans[(0, 1, 0)] = 4
ans[(1, 0, 0)] = 4
ans[(0, 1, 1)] = 4
ans[(1, 0, 1)] = 4
ans[(1, 1, 0)] = 4
ans[(1, 1, 1)] = 5
ans[(0, 0, 2)] = 5
ans[(0, 2, 0)] = 5
ans[(2, 0, 0)] = 5
ans[(0, 1, 2)] = 5
ans[(0, 2, 1)] = 5
ans[(1, 0, 2)] = 5
ans[(1, 2, 0)] = 5
ans[(2, 0, 1)] = 5
ans[(2, 1, 0)] = 5
ans[(1, 1, 2)] = 6
ans[(1, 2, 1)] = 6
ans[(2, 1, 1)] = 6
ans[(0, 2, 2)] = 6
ans[(2, 0, 2)] = 6
ans[(2, 2, 0)] = 6
ans[(1, 2, 2)] = 7
ans[(2, 1, 2)] = 7
ans[(2, 2, 1)] = 7
ans[(2, 2, 2)] = 8


def dist(A, B):
    return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5


def equal(A, B):
    return dist(A, B) < eps


def belong(P, i):
    return abs(dist(P, (c[i][0], c[i][1])) - c[i][2]) < eps


def intersection(c1, c2):
    O1 = c1[0], c1[1]
    O2 = c2[0], c2[1]
    r1, r2 = c1[2], c2[2]
    OO = (O2[0] - O1[0], O2[1] - O1[1])
    d = dist(O1, O2)
    if d > r1 + r2 or d < abs(r1 - r2):
        return []
    alp = atan2(OO[1], OO[0])
    phi = acos((r1**2 + d**2 - r2**2) / (2 * r1 * d))
    P1 = (r1 * cos(alp + phi) + O1[0], r1 * sin(alp + phi) + O1[1])
    P2 = (r1 * cos(alp - phi) + O1[0], r1 * sin(alp - phi) + O1[1])
    if equal(P1, P2):
        return [P1]
    return [P1, P2]


def solve():
    if n == 1:
        return 2
    if n == 2:
        res = 3
        inter = intersection(c[0], c[1])
        if len(inter) == 2:
            res += 1
        return res
    cnt = 0
    inter = [0, 0, 0]
    p = []
    for i in range(3):
        for j in range(i + 1, 3):
            cur = intersection(c[i], c[j])
            for P in cur:
                p.append(P)
                inter[i + j - 1] += 1
    for P in p:
        flag = 1
        for i in range(3):
            if not belong(P, i):
                flag = 0
        if flag:
            cnt += 1
    res = ans[tuple(inter)] - cnt // 3
    return res


n = int(input())
c = [tuple(map(int, input().split())) for i in range(n)]
print(solve())
