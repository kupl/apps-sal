def __starting_point():
    n = int(input())
    topodds = 0
    bottomodds = 0
    flipabble = False
    for _ in range(n):
        top, bottom = list(map(int, input().split()))
        if not flipabble and (top + bottom) % 2 != 0:
            flipabble = True
        topodds += 0 if (top % 2 == 0) else 1
        bottomodds += 0 if (bottom % 2 == 0) else 1
    if (topodds + bottomodds) % 2 != 0:
        print(-1)
    elif (topodds % 2 != 0) or (bottomodds % 2 != 0):
        print(1 if flipabble else -1)
    else:
        print(0)


__starting_point()
