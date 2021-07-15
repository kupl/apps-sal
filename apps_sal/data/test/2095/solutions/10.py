def __starting_point():
    n = int(input())

    good = []
    for i in range(n):
        for j, x in enumerate(map(int, input().split())):
            if j != i and x in (1, 3):
                break
        else:
            good.append(i + 1)

    print(len(good))
    if good:
        print(' '.join(map(str, good)))
__starting_point()
