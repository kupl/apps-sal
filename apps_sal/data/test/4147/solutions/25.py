from itertools import product
(n, a, b, c) = list(map(int, input().split()))
L = [int(input()) for _ in range(n)]
INF = 10 ** 18
ans = INF
for subset in product(list(range(4)), repeat=n):
    cost = 0
    ABC = [[] for _ in range(3)]
    for (i, s) in enumerate(subset):
        if not s:
            continue
        ABC[s - 1].append(L[i])
    if any((not X for X in ABC)):
        continue
    for (x, X) in zip((a, b, c), ABC):
        cost += (len(X) - 1) * 10
        cost += abs(x - sum(X))
    if cost < ans:
        ans = cost
print(ans)
