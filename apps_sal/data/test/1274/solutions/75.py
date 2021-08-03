import heapq


def main():
    n, m = map(int, input().split())
    data = {}
    priorityQ = []
    for _ in range(n):
        a, b = map(int, input().split())
        if m + 1 - a >= 0:
            if m + 1 - a in data:
                data[m + 1 - a].append(b)
            else:
                data[m + 1 - a] = [b]
    ans = 0
    for i in range(m, 0, -1):
        if i in data.keys():
            for k in data[i]:
                heapq.heappush(priorityQ, -k)
        if priorityQ:
            ans -= heapq.heappop(priorityQ)
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
