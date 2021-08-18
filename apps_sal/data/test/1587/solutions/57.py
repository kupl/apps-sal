def __starting_point():
    n = int(input())
    s = list(input())

    ss = sorted(s)

    cnt = 0
    if "W" in s:
        sind = ss.index("W")

        cnt = 0
        for i in range(sind):
            if s[i] == "W":
                cnt += 1

    print(cnt)


__starting_point()
