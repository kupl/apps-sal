from collections import deque


def main():
    # N = int(input())
    # N,= [int(a) for a in input().split()]
    # N, M = [int(a) for a in input().split()]

    # a = []
    # # b = []
    # c = []
    #
    # for _ in range(M):
    #     aa, bb = [int(a) for a in input().split()]
    #     cc = [int(a) for a in input().split()]
    #     a.append(aa)
    #     # b.append(bb)
    #     c.append(cc)
    N, M = [int(a) for a in input().split()]

    AB = [
        [int(a) for a in input().split()]
        for _ in range(M)
    ]

    pp = [[] for _ in range(N)]
    for a, b in AB:
        pp[a - 1].append(b - 1)

    startpool = set(range(N))

    result = None

    while len(startpool) != 0:
        start = min(startpool)

        q = deque([(start, [start])])
        renketu = {start}
        while len(q) != 0:
            p, history = q.popleft()
            target = pp[p]
            for t in target:
                if t in history:
                    if result is None:
                        result = history
                    elif len(result) > len(history) - history.index(t):
                        result = history[history.index(t):]
                if t not in renketu:
                    q.append([t, history + [t]])

                renketu.add(t)
        startpool -= renketu

    if result is not None:
        print((len(result)))
        for a in result:
            print((a + 1))
        return
    else:
        print((-1))


def __starting_point():
    main()


__starting_point()
