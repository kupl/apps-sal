N = int(input())
A = list(map(int, input().split()))
AI = sorted(((a, i) for (i, a) in enumerate(A, 1)), reverse=True)


def solve(a, i, prev):
    (pl, pr, ps) = (i, 0, 0)
    for (l, r, s) in prev:
        yield (l, r - 1, max(s + abs(r - i) * a, ps + abs(i - pl) * a))
        (pl, pr, ps) = (l, r, s)
    yield (pl + 1, pr, ps + abs(i - pl) * a)


prev = [(1, N, 0)]
for (a, i) in AI:
    prev = [*solve(a, i, prev)]
print(max((s for (l, r, s) in prev)))
