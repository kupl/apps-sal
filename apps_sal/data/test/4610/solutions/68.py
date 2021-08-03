import bisect as bs
N, K = (int(x) for x in input().split())
A = sorted([int(x) for x in input().split()])
def f(X, x): return bs.bisect_right(X, x) - bs.bisect_left(X, x)


cnt = sorted([f(A, a) for a in set(A)], reverse=True)
vrt = len(cnt)
print(sum(cnt[K:]) if vrt > K else 0)
