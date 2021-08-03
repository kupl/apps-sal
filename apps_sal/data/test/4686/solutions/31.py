from collections import Counter


def answer(w: str) -> str:
    counts = list(Counter(w).values())
    for count in counts:
        if count % 2 == 1:
            return 'No'

    return 'Yes'


def main():
    w = input()
    print((answer(w)))


def __starting_point():
    main()


__starting_point()
