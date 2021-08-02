N, M, Q = map(int, input().split())
a = []
b = []
c = []
d = []
for _ in range(Q):
    ad, bd, cd, dd = map(int, input().split())
    a.append(ad - 1)
    b.append(bd - 1)
    c.append(cd)
    d.append(dd)


def score(A):
    tmp = 0
    for ai, bi, ci, di in zip(a, b, c, d):
        if A[bi] - A[ai] == ci:
            tmp += di
    return tmp


def dfs(A):
    if len(A) == N:
        return score(A)
    res = 0
    prev_last = A[-1] if len(A) > 0 else 0
    for v in range(prev_last, M):
        A.append(v)
        res = max(res, dfs(A))
        A.pop()
    return res


print(dfs([]))
