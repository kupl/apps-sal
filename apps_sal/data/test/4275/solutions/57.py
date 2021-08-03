def main():
    sample = input()
    if sample[2] == sample[3] and sample[4] == sample[5]:
        return "Yes"
    return "No"


def __starting_point():
    print(main())


__starting_point()
