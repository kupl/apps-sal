3


def main():
    s = input()

    has_dot = False
    zero = True
    first_non_zero = 0
    last_non_zero = 0
    sep = len(s)

    for i, c in enumerate(s):
        if c != "0":
            if c == ".":
                sep = i
                has_dot = True
            elif zero:
                zero = False
                first_non_zero = i
                last_non_zero = i
            else:
                last_non_zero = i

    b = sep - first_non_zero
    if b > 0:
        b -= 1
    a = s[first_non_zero: last_non_zero + 1]
    a = "".join(a.split("."))
    if len(a) > 1:
        a = (a[0] + "." + a[1:])

    print((a if not zero else "0") + (("E" + str(b)) if b != 0 else ""))


def __starting_point():
    main()


__starting_point()
