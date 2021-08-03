def read_nums():
    return [int(x) for x in input().split()]


def compute_min_cost(t, nums):
    res = 0
    for num in nums:
        if abs(t - num) <= 1:
            continue
        res += abs(num - t) - 1
    return res


def main():
    _ = read_nums()

    costs = []
    nums = read_nums()
    for t in range(1, 101):
        min_cost = compute_min_cost(t, nums)
        costs.append((t, min_cost))

    t, cost = sorted(costs, key=lambda x: x[1])[0]
    print(t, cost)


def __starting_point():
    main()


__starting_point()
