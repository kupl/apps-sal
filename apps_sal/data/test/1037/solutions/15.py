from operator import itemgetter as get
N = int(input())
A = list(map(int, input().split()))
SB = 0
ABI = sorted((((b := (max(N - i, i - 1) * a)), (SB := (SB + b))) and (a, b, i) for (i, a) in enumerate(A, 1)), reverse=True)


def solve(a, i, prev, th):
    (pl, pr, ps) = (0, -1, 0)
    for (l, r, s) in prev:
        if s < th:
            continue
        if pr == r - 1:
            yield (l, r - 1, max(s + abs(r - i) * a, ps + abs(i - pl) * a))
        else:
            if pl:
                yield (pl + 1, pr, ps + abs(i - pl) * a)
            yield (l, r - 1, s + abs(r - i) * a)
        (pl, pr, ps) = (l, r, s)
    yield (pl + 1, pr, ps + abs(i - pl) * a)


prev = [(1, N, 0)]
pm = 0
for (j, (a, b, i)) in enumerate(ABI):
    M = 0
    prev = [((M := max(M, s)),) and (l, r, s) for (l, r, s) in solve(a, i, prev, pm - SB)]
    pm = M
    SB -= b
print(pm)
