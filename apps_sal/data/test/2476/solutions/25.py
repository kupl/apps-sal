from collections import Counter
import bisect
import sys
stdin = sys.stdin


def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def nn(): return list(stdin.readline().split())
def ns(): return stdin.readline().rstrip()


n = ni()
a = na()

c = sorted(Counter(a).values())
cc = [0]
m = len(c)
for i in c:
    cc.append(cc[-1] + i)


def is_ok(k, arg):
    b = bisect.bisect_right(c, arg)
    p = cc[b] + (m - b) * arg
    return True if p >= arg * k else False


for k in range(1, n + 1):
    if k > m:
        print((0))
        continue
    ok, ng = -1, n // k + 1
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(k, mid):
            ok = mid
        else:
            ng = mid

    print(ok)
