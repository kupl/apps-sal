def main():
    a = []
    for i in range(4):
        a.append(tuple(map(int, input().split())))

    car = [0] * 4

    for i, (l, s, r, p) in enumerate(a):

        car[i] += l
        car[(i - 1) % 4] += l

        car[i] += r
        car[(i + 1) % 4] += r

        car[i] += s
        car[(i + 2) % 4] += s

    for i in range(4):
        if car[i] > 0 and a[i][3] == 1:
            print("YES")
            return

    print("NO")


def __starting_point():
    main()


__starting_point()
