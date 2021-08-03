import heapq


def main():
    n, k = map(int, input().split())
    power = list(map(int, input().split()))
    coins = list(map(int, input().split()))

    power_coins = sorted(zip(power, coins))
    result = {power[i]: coins[i] for i in range(n)}
    kills = 0
    coins = 0
    min_heap = []
    for p, c in power_coins:
        result[p] += coins
        if kills < k:
            kills += 1
            heapq.heappush(min_heap, c)
            coins += c
        elif k > 0:
            if c > min_heap[0]:
                coins -= min_heap[0]
                coins += c
                heapq.heapreplace(min_heap, c)
    print(' '.join(str(result[p]) for p in power))


main()
