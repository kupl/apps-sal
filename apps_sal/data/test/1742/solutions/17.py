def __starting_point():
    n, m = (int(x) for x in input().split())
    queue = [int(x) - 1 for x in input().split()]
    id___passables = [set() for _ in range(n)]
    for _ in range(m):
        id1, id2 = (int(x) - 1 for x in input().split())
        id___passables[id2].add(id1)
    train_passables = id___passables[queue[-1]].copy()
    ans = 0
    for person in reversed(queue[:-1]):
        if person in train_passables:
            ans += 1
        else:
            train_passables &= id___passables[person]
    print(ans)


__starting_point()
