def main():
    aa, bb = input(), input()
    print(("NO", "YES")[len(aa) == len(bb) and any(c == "1" for c in aa) == any(c == "1" for c in bb)])


def __starting_point():
    main()

__starting_point()
