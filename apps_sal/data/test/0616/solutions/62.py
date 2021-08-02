def main():
    import numpy as np

    n, m = list(map(int, input().split()))
    dp = np.full(2**n, 10**9, dtype=np.int64)
    dp[0] = 0
    opened = np.arange(2**n)

    for _ in range(m):
        cost, types = list(map(int, input().split()))
        to_open = np.array(list(map(int, input().split())), dtype=np.int64)

        openable = np.left_shift(1, to_open - 1).sum()
        new_indexes = opened | openable
        new_costs = dp + cost
        sort_index = np.argsort(new_costs)
        new_costs.sort()
        update_pattern, idx = np.unique(new_indexes[sort_index], return_index=True)
        update_cost = new_costs[idx]
        dp[update_pattern] = np.minimum(dp[update_pattern], update_cost)

    full_open = 2**n - 1
    ans = dp[full_open]
    if ans == 10 ** 9:
        ans = -1

    print(ans)


def __starting_point():
    main()


__starting_point()
