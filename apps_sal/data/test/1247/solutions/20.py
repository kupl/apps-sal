def main():
    l = [0] * 26
    for c in input():
        l[ord(c) - 97] ^= 1
    x = l.count(1)
    print(('Second', 'First')[not x or x & 1])


def __starting_point():
    main()
__starting_point()
