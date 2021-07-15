import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: map(int, sys.stdin.readline().split())
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

N = ini()
A = inl()
amax = max(A)
imax = A.index(amax)
amin = min(A)
imin = A.index(amin)


def make_positive():
    nonlocal amax, imax
    ans = []
    assert amax >= 0
    for i in range(N):
        if i > 0 and A[i] < 0:
            ans.append((imax, i))
            A[i] += amax
            assert A[i] >= 0
    for i in range(1, N):
        if A[i] < A[i - 1]:
            ans.append((imax, i))
            A[i] += amax
            assert A[i] >= A[i - 1]
            if A[i] > amax:
                amax = A[i]
                imax = i
    assert len(ans) <= 2 * N
    print(len(ans))
    for x, y in ans:
        print(x + 1, y + 1)


def make_negative():
    nonlocal amin, imin
    ans = []
    assert amin <= 0
    for i in range(N):
        if i < N - 1 and A[i] > 0:
            ans.append((imin, i))
            A[i] += amin
            assert A[i] <= 0
    for i in range(N - 2, -1, -1):
        if A[i] > A[i + 1]:
            ans.append((imin, i))
            A[i] += amin
            assert A[i] <= A[i + 1]
            if A[i] < amin:
                amin = A[i]
                imin = i
    assert len(ans) <= 2 * N
    print(len(ans))
    for x, y in ans:
        print(x + 1, y + 1)


def solve():
    if abs(amax) > abs(amin):
        make_positive()
    else:
        make_negative()
    return


solve()

