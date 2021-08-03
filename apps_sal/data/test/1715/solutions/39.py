import bisect  # bisect.bisect_left(B, a)
import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini] * i for _ in range(j)]


# from collections import defaultdict #d = defaultdict(int) d[key] += value
# from collections import Counter # a = Counter(A).most_common()
# from itertools import accumulate #list(accumulate(A))

A, B, Q = mi()

S = [ii() for _ in range(A)]
T = [ii() for _ in range(B)]

S_ = [S[0]] + S + [S[A - 1]]
T_ = [T[0]] + T + [T[B - 1]]

for _ in range(Q):
    f = ii()
    to_s = bisect.bisect_left(S, f)
    to_t = bisect.bisect_left(T, f)

    ans = float('inf')

    for i in [S_[to_s], S_[to_s + 1]]:
        for j in [T_[to_t], T_[to_t + 1]]:
            tmp = min(abs(i - f), abs(j - f)) + abs(i - j)
            ans = min(ans, tmp)
    '''
    ans = min(abs(S_[to_s+1] - f) + abs(S_[to_s+1] - T_[to_t+1]), float('inf'))
    ans = min(abs(S_[to_s+1] - T_[to_t+1]) + abs(f - T_[to_t+1]), ans)
    ans = min(abs(S_[to_s+1] - f) + abs(S_[to_s+1] - T_[to_t]), ans)
    ans = min(abs(S_[to_s+1] - T_[to_t]) + abs(f - T_[to_t]), ans)
    ans = min(abs(S_[to_s] - f) + abs(S_[to_s] - T_[to_t+1]), ans)
    ans = min(abs(S_[to_s] - T_[to_t+1]) + abs(f - T_[to_t+1]), ans)
    ans = min(abs(S_[to_s] - f) + abs(S_[to_s] - T_[to_t]), ans)
    ans = min(abs(S_[to_s] - T_[to_t]) + abs(f - T_[to_t]), ans)
    '''
    print(ans)
