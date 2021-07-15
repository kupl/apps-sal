def main():
    n, m = list(map(int, input().split()))
    all_patterns = 2**n
    DP = [10**9] * all_patterns
    DP[0] = 0
    for _ in range(m):
        cost, types = list(map(int, input().split()))
        to_open = list(map(int, input().split()))

        openable = 0
        for open in to_open:
            openable += 1 << (open-1)

        for opened in range(all_patterns):
            pattern = opened | openable
            new_cost = DP[opened] + cost
            if DP[pattern] > new_cost:
                DP[pattern] = new_cost

    full_open = 2**n - 1
    ans = DP[full_open]
    if ans == 10 ** 9:
        ans = -1
        
    print(ans)


def __starting_point():
    main()

__starting_point()
