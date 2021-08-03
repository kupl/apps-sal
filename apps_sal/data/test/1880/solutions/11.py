def __starting_point():

    s = [c for c in input()]
    ss = s[0] + s[2] + s[4] + s[3] + s[1]
    num = int(ss)

    print(str(num**5)[-5:])


__starting_point()
