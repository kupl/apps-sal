from collections import deque


def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = deque(list(map(lambda x: int(x) - 1, input().split())))
    tmp = set()
    for p1, p in enumerate(a):
        p2 = p[0]
        if p1 == a[p2][0]:
            tmp.add(p1)
            tmp.add(p2)
    q = deque(tmp)
    for i in tmp:
        a[i].popleft()

    day = 0
    while True:
        day += 1
        tmp = set()
        while q:
            p1 = q.popleft()
            if len(a[p1]) == 0:
                continue
            p2 = a[p1][0]
            if p1 == a[p2][0]:
                tmp.add(p1)
                tmp.add(p2)
        q = deque(tmp)
        for i in tmp:
            a[i].popleft()
        tmp = set()
        if len(q) == 0:
            break

    for i in a:
        if i:
            print(-1)
            return
    print(day)


def __starting_point():
    main()


__starting_point()
