def __starting_point():
    N = int(input())
    tasks = []
    for _ in range(N):
        (a, b) = list(map(int, input().split()))
        tasks.append((b, a))
    tasks.sort()
    t = 0
    for (b, a) in tasks:
        if t + a > b:
            break
        t += a
    else:
        print('Yes')
        return
    print('No')


__starting_point()
