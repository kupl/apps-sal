import heapq


def __main__(n, k):
    servers = [0] * k
    times = []

    for i in range(n):
        s, m = list(map(int, input().split()))
        time = max(servers[0], s)
        heapq.heapreplace(servers, time + m)
        times.append(time + m)

    print('\n'.join(str(time) for time in times))


def __starting_point():
    n, k = list(map(int, input().split()))
    __main__(n, k)


__starting_point()
