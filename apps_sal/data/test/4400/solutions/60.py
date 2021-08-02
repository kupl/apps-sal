def main():
    s = input()
    cnt = s.count("R")
    if s[1] == "R":
        print(cnt)
    else:
        print(min(cnt, 1))
    return


def __starting_point():
    main()


__starting_point()
