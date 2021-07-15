def main():
    aa, bb = input(), input()
    print(("NO", "YES")[len(aa) == len(bb) and ("1" in aa) == ("1" in bb)])


def __starting_point():
    main()

__starting_point()
