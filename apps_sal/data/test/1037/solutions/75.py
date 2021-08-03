N = int(input())


def left(a, i, prev):
    yield 0
    for l, s in enumerate(prev, 1 - i):
        yield s + abs(l) * a


def right(a, i, prev):
    for r, s in enumerate(prev, N - len(prev) - i + 1):
        yield s + abs(r) * a
    yield 0


pd = [0]
A = list(map(int, input().split()))
for a, i in sorted(((a, i) for i, a in enumerate(A, 1)), reverse=True):
    pd = [*list(map(max, list(zip(left(a, i, pd), right(a, i, pd)))))]

print((max(pd)))
