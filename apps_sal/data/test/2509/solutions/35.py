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


def dp3(ini, i, j, k):
    return [[[ini] * i for _ in range(j)] for _ in range(k)]


(N, K) = mi()
cnt = 0
for b in range(K + 1, N + 1):
    for x in range((N - K) // b + 1):
        if b * x + K == 0:
            cnt -= 1
        cnt += min(N - (b * x + K) + 1, b - K)
print(cnt)
