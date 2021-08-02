from bisect import *
import sys


def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


def solve():
    dp = [[0] * (w + 1) for _ in range(w + 1)]
    for d in range(1, w + 1):
        for l in range(w - d + 1):
            r = l + d
            cnt = [0] * (w + 1)
            for i in range(h):
                sl = bisect_left(seg[i], l)
                sr = bisect_right(seg[i], r)
                if sl == sr:
                    continue
                b = seg[i][sl]
                e = seg[i][sr - 1]
                cnt[b] += 1
                cnt[e] -= 1
            #for j in range(l, r): cnt[j + 1] += cnt[j]
            # print(cnt)
            #mx = max(cnt)
            # if mx == 0: continue
            for j in range(l, r):
                cnt[j + 1] += cnt[j]
                if cnt[j] == 0:
                    continue
                dp[l][r] = max(dp[l][r], cnt[j] ** 2 + dp[l][j] + dp[j + 1][r])
    print(dp[0][w])
    # p2D(dp)


h, w = MI()
seg = [[0] for _ in range(h)]
for i in range(h):
    for _ in range(II()):
        l, r = MI()
        seg[i].append(r)
solve()
