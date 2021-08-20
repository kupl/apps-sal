from itertools import product


def convert(x, pt):
    return sum((e if p else -e for (e, p) in zip(x, pt)))


def submit():
    (n, m) = (int(a) for a in input().split())
    cakes = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0
    for pt in product([0, 1], repeat=3):
        pt_cakes = [convert(c, pt) for c in cakes]
        pt_cakes.sort(reverse=True)
        pt_sum = sum(pt_cakes[:m])
        if pt_sum > ans:
            ans = pt_sum
    print(ans)


submit()
