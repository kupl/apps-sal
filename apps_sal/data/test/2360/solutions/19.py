import heapq


def tea_list(students):
    teatimes = [0] * len(students)
    events = []
    for (i, (a, l)) in enumerate(students):
        events.append((a, 0, (a, i, l)))
    heapq.heapify(events)
    queue_len = 0
    while events:
        (t, etype, e) = heapq.heappop(events)
        if etype == 0:
            (a, i, l) = e
            if a + queue_len <= l:
                heapq.heappush(events, (a + queue_len, 1, i))
                queue_len += 1
        elif etype == 1:
            queue_len -= 1
            teatimes[e] = t
    return teatimes


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        students = [tuple((int(x) for x in input().split())) for _ in range(N)]
        print(*tea_list(students))


def __starting_point():
    main()


__starting_point()
