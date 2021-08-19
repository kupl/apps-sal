from functools import lru_cache
import sys
input = sys.stdin.readline

n, T = list(map(int, input().split()))
S = [list(map(int, input().split())) for i in range(n)]

DP = [[0] * (4) for i in range(T + 1)]
mod = 10**9 + 7


@lru_cache(maxsize=None)
def calc(used, recent, time):
    ANS = 0
    for i in range(n):
        # print(i,used)
        if i in used:
            continue
        if time + S[i][0] > T:
            continue
        if S[i][1] == recent:
            continue
        if time + S[i][0] == T:
            ANS += 1
        if time + S[i][0] < T:
            used2 = list(used) + [i]
            used2.sort()
            recent2 = S[i][1]
            time2 = time + S[i][0]
            ANS = (ANS + calc(tuple(used2), recent2, time2)) % mod

    return ANS


print(calc(tuple(), -1, 0) % mod)
