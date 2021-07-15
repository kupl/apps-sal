def answer(w: int, a: int, b: int) -> int:
    b_a = abs(b - a)
    if b_a <= w:
        return 0
    return b_a - w


def main():
    w, a, b = map(int, input().split())
    print(answer(w, a, b))


def __starting_point():
    main()
__starting_point()
