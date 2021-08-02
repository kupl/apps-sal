from itertools import product


def solve():
    N, A, B, C, *L = list(map(int, open(0).read().split()))

    ans = float("inf")
    for X in product([0, 1], repeat=N):
        tmp = [L[i] for i in range(N) if X[i]]
        if len(tmp) < 3:
            continue
        for Y in product([0, 1, 2], repeat=len(tmp)):
            tmp_inner = [[] for _ in range(3)]
            for j, y in enumerate(Y):
                tmp_inner[y].append(tmp[j])
            if all(t for t in tmp_inner):
                join_cost = sum((len(li) - 1) * 10 for li in tmp_inner)
                expand_cost = sum(abs(sum(t) - a) for t, a in zip(tmp_inner, [A, B, C]))
                ans = min(ans, join_cost + expand_cost)
    return ans


print((solve()))
