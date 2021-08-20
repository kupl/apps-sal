def main():
    import heapq
    (n, m, s) = map(int, input().split())
    edges = [[] for _ in range(n)]
    max_cost = 0
    for _ in range(m):
        (from_, to, cost, time) = map(int, input().split())
        edges[from_ - 1].append((to - 1, cost, time))
        edges[to - 1].append((from_ - 1, cost, time))
        if cost > max_cost:
            max_cost = cost
    banks = []
    for i in range(n):
        (coin, time) = map(int, input().split())
        banks.append((coin, time))
    max_coin = max_cost * (n - 1)
    if s > max_coin:
        s = max_coin
    INF = float('INF')
    DP = [[INF] * (max_coin + 1) for _ in range(n)]
    DP[0][s] = 0

    def push_todo(node, coin, time):
        if coin < 0:
            return
        if time >= DP[node][coin]:
            return
        heapq.heappush(todo, (time, node, coin))
        DP[node][coin] = time

    def charge(node, current_coin, current_time):
        (coin, time) = banks[node]
        new_coin = current_coin + coin
        if new_coin > max_coin:
            new_coin = max_coin
        push_todo(node, new_coin, current_time + time)
    todo = [(0, 0, s)]
    while todo:
        (current_time, node, current_coin) = heapq.heappop(todo)
        if current_time > DP[node][current_coin]:
            continue
        charge(node, current_coin, current_time)
        for (to, cost, time) in edges[node]:
            push_todo(to, current_coin - cost, current_time + time)
    for node in range(1, n):
        print(min(DP[node]))


def __starting_point():
    main()


__starting_point()
