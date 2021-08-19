def main():
    (n, m) = list(map(int, input().split()))
    DP = [10 ** 9] * 2 ** n
    DP[0] = 0
    updated_patterns = {0}
    for _ in range(m):
        (cost, types) = list(map(int, input().split()))
        to_open = list(map(int, input().split()))
        openable = 0
        for open in to_open:
            openable += 1 << open - 1
        new_updated = set()
        for opened in updated_patterns:
            pattern = opened | openable
            new_cost = DP[opened] + cost
            if DP[pattern] > new_cost:
                DP[pattern] = new_cost
                new_updated.add(pattern)
        updated_patterns |= new_updated
    full_open = 2 ** n - 1
    ans = DP[full_open]
    if ans == 10 ** 9:
        ans = -1
    print(ans)


def __starting_point():
    main()


__starting_point()
