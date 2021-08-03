def __starting_point():
    input()
    days = input()

    m = {}
    m["SF"] = 0
    m["FS"] = 0
    loc = days[0]
    for d in days:
        if loc != d:
            m[loc + d] += 1
            loc = d

    if m["SF"] > m["FS"]:
        print("YES")
    else:
        print("NO")


__starting_point()
