def __starting_point():

    hh, mm = map(int, input().split(sep=":"))
    a = int(input())

    hh += a // 60
    mm += a % 60

    hh += mm // 60
    mm = mm % 60

    hh = hh % 24

    # print(hh,mm)

    strhh = "0" * (2 - len(str(hh))) + str(hh)
    strmm = "0" * (2 - len(str(mm))) + str(mm)
    print(strhh, ":", strmm, sep="")


__starting_point()
