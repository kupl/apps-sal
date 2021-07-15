import sys; sys.setrecursionlimit(1000000)
def solve():
    MOD = 1000000007
    n,m, = rv()
    on, = rl(1)
    on.sort()
    res = 1
    distances = list()
    for i in range(0, m + 1):
        first = on[i - 1] - 1 if i > 0 else 0
        second = on[i] - 1 if i < m else n - 1
        val = second - first - (1 if (i > 0 and i < m) else 0)
        distances.append(val)
    for i in range(1, n - m + 1):
        res *= i
    for val in distances:
        for i in range(1, val + 1):
            res //= i
    res %= MOD
    for i in range(1, len(distances) - 1):
        for j in range(distances[i] - 1):
            res *= 2
            res %= MOD
    print(res)


def rv(): return list(map(int, input().split()))
def rl(n): return [list(map(int, input().split())) for _ in range(n)]
if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
solve()



