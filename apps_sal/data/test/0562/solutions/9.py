def main():
    n = int(input())
    events = []
    for _ in range(n):
        (l, r) = (int(x) for x in input().split())
        events.append((l, 1))
        events.append((r + 1, -1))
    cur = 0
    for (_, event) in sorted(events):
        cur += event
        if cur > 2:
            print('NO')
            break
    else:
        print('YES')


def __starting_point():
    main()


__starting_point()
