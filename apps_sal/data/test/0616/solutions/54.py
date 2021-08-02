

def main():
    n, m = list(map(int, input().split()))

    L = 2**n

    cost = [0] + [10**8 for i in range(L - 1)]

    for _ in range(m):
        a, b = list(map(int, input().split()))

        c = sum([2**(int(x) - 1) for x in input().split()])
        for i in range(L):
            q = c | i
            cost[q] = min(cost[q], cost[i] + a)
    print((cost[L - 1] if cost[L - 1] < 10**8 else -1))


def __starting_point():
    main()


__starting_point()
