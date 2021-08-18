from itertools import accumulate
import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)


def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


n, m = li()
a = list(li_())

ans = [0] * m
cnt_equal = [0] * m
for i in range(n - 1):
    cnt_equal[a[i + 1]] += (((a[i + 1] + m - a[i]) % m) - 1)

cnt_inner = [0] * (2 * m + 1)
for i in range(n - 1):
    cnt_inner[a[i] + 1] += 1
    cnt_inner[a[i] + (a[i + 1] + m - a[i]) % m] -= 1

cnt_inner = list(accumulate(cnt_inner))
cnt_inner = [cnt_inner[i] + cnt_inner[i + m] for i in range(m)]


fav = 0
for i in range(n - 1):
    ans[0] += min((a[i + 1] + m - a[i]) % m, 1 + (a[i + 1] + m - fav) % m)

for fav in range(1, m):
    ans[fav] = ans[fav - 1] + cnt_equal[fav - 1] - cnt_inner[fav - 1]

print(min(ans))
