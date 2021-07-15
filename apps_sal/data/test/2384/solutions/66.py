import collections, sys
sys.setrecursionlimit(100005)
N = int(input())
A = [int(_) for _ in input().split()]
INF = float('inf')
memo = collections.defaultdict(lambda: INF)


def c(start, res):
    if memo[start, res] != INF:
        return memo[start, res]
    elif 2 * res - 1 > N - start:
        memo[start, res] = -INF
    elif start >= N:
        memo[start, res] = -INF
    elif res > 1:
        memo[start, res] = max(A[start] + c(start + 2, res - 1),
                               c(start + 1, res), c(start + 2, res))
    else:
        memo[start, res] = max(A[start], c(start + 1, res))
    return memo[start, res]


print((c(0, N // 2)))

