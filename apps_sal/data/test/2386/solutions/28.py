(N, *A) = list(map(int, open(0).read().split()))
if N == 1:
    print(0)
else:
    cs = [a - i for (i, a) in enumerate(A)]
    cs.sort()
    n = len(cs)
    half = n // 2
    d1 = -cs[half]
    d2 = -cs[half + 1]
    sad1 = sum([abs(c + d1) for c in cs])
    sad2 = sum([abs(c + d2) for c in cs])
    print(min(sad1, sad2))
