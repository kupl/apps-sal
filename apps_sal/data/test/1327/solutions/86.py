import sys
sys.setrecursionlimit(10 ** 8)


def ii():
    return int(sys.stdin.readline())


def mi():
    return map(int, sys.stdin.readline().split())


def li():
    return list(map(int, sys.stdin.readline().split()))


def li2(N):
    return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def dp2(ini, i, j):
    return [[ini] * i for _ in range(j)]


(N, M) = mi()
xyz = li2(N)
sign = [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1], [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]
ans = 0
for i in range(8):
    A = [sum((xyz[x][k] * sign[i][k] for k in range(3))) for x in range(N)]
    A = sorted(A, reverse=True)
    ans = max(ans, sum(A[:M]))
print(ans)
