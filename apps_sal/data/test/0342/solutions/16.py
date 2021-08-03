
def main():
    buf = input()
    buflist = buf.split()
    A = int(buflist[0])
    B = int(buflist[1])
    C = int(buflist[2])
    length = 2 * C
    length += 2 * min(A, B)
    u = min(A, B)
    A -= u
    B -= u
    if A > 0 or B > 0:
        length += 1
    print(length)


def __starting_point():
    main()


__starting_point()
