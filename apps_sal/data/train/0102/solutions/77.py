def main():
    best = []
    for i in range(1, 20):
        for j in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            best.append(int(j * i))

    m = int(input())

    for i in range(m):
        n = int(input())
        t = 0
        for j in best:
            if n >= j:
                t += 1
        print(t)


def __starting_point():
    main()


__starting_point()
