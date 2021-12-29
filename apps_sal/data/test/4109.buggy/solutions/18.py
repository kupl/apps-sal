import numpy as np
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    (n, m, x) = list(map(int, input().split()))
    data = np.array(read().split(), np.int64)
    data = data.reshape(n, -1)
    cost_per_cost = data[:, 0]
    effect_per_book = data[:, 1:]
    costs = np.zeros(2 ** n, np.int64)
    ability = np.zeros((2 ** n, m), np.int64)
    for i in range(n):
        costs[1 << i:1 << i + 1] = costs[:1 << i] + cost_per_cost[i]
        ability[1 << i:1 << i + 1] = ability[:1 << i] + effect_per_book[i]
    ok = np.all(ability >= x, axis=1)
    res = costs[ok]
    if len(res) == 0:
        print(-1)
    else:
        print(res.min())


def __starting_point():
    main()


__starting_point()
