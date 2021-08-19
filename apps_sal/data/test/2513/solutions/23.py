def main():
    n = int(input())
    s = input()
    for t in ["SS", "SW", "WS", "WW"]:
        for i in s[1:-1]:
            if t[-1] == "S":
                if i == "o":
                    t += t[-2]
                else:
                    t += "S" if t[-2] == "W" else "W"
            else:
                if i == "x":
                    t += t[-2]
                else:
                    t += "S" if t[-2] == "W" else "W"
        # check1
        if t[0] == "S":
            if s[0] == "o":
                f = t[-1] == t[1]
            else:
                f = t[-1] != t[1]
        else:
            if s[0] == "x":
                f = t[-1] == t[1]
            else:
                f = t[-1] != t[1]

        # check2
        if t[-1] == "S":
            if s[-1] == "o":
                g = t[-2] == t[0]
            else:
                g = t[-2] != t[0]
        else:
            if s[-1] == "x":
                g = t[-2] == t[0]
            else:
                g = t[-2] != t[0]

        if f and g:
            print(t)
            break

    else:
        print((-1))


def __starting_point():
    main()


__starting_point()
