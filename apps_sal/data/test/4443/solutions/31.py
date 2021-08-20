def solve(C: str):
    return chr(ord(C) + 1)


def main():
    C = input().strip()
    answer = solve(C)
    print(answer)


def __starting_point():
    main()


__starting_point()
