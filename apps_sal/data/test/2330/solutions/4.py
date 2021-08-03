def solve(n, m, costs):
    if n == 2:
        print(-1)
        return

    if m < n:
        print(-1)
        return

    cost = 0
    for i in range(n - 1):
        cost += costs[i] + costs[i + 1]

    # print(cost)
    cost += costs[0] + costs[-1]
    min_cost = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            cost1 = costs[i] + costs[j]
            if cost < min_cost:
                min_cost = cost1
                min_pair = [i + 1, j + 1]

    m -= n
    cost += m * min_cost
    print(cost)
    for i in range(n - 1):
        print(i + 1, i + 2)

    print(n, 1)
    for i in range(m):
        print(min_pair[0], min_pair[1])


def main():
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().split()))
        costs = list(map(int, input().split()))
        solve(n, m, costs)


main()
