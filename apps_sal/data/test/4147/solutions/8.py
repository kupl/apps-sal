from itertools import product


def solve():
    (N, A, B, C, *L) = list(map(int, open(0).read().split()))
    ans = float('inf')
    for X in product([0, 1, 2, 3], repeat=N):
        tmp = [[] for _ in range(3)]
        [tmp[x - 1].append(L[i]) for (i, x) in enumerate(X) if x]
        if any((not t for t in tmp)):
            continue
        join_cost = sum(((len(li) - 1) * 10 for li in tmp))
        expand_cost = sum((abs(sum(t) - a) for (t, a) in zip(tmp, [A, B, C])))
        ans = min(ans, join_cost + expand_cost)
    return ans


print(solve())
