def main():
    bw = [0, 0]
    for _ in range(8):
        for c in input():
            if c.isalpha():
                bw[c.isupper()] += {'Q': 9, 'R': 5, 'B': 3, 'N': 3, 'P': 1, 'K': 0}[c.upper()]
    if bw[0] < bw[1]:
        print("White")
    elif bw[0] > bw[1]:
        print("Black")
    else:
        print("Draw")


def __starting_point():
    main()
__starting_point()
