def main():
    a, b = list(map(int, input().split()))

    dif = 1
    while True:
        if dif % 2 == 1:
            if a >= dif:
                a -= dif
            else:
                print("Vladik")
                return
        else:
            if b >= dif:
                b -= dif
            else:
                print("Valera")
                return
        dif += 1


def __starting_point():
    main()


__starting_point()
