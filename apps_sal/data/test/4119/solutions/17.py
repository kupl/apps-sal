from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return list(zip(a, b))


N, M, *X = list(map(int, open(0).read().split()))
if N >= M:
    print((0))
    return

X.sort()
diffs = [cur - prev for prev, cur in pairwise(X)]
diffs.sort()
print((sum(diffs[: M - N])))

