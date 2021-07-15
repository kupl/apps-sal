def answer(x: int, y: int, z: int) -> int:
    return len(range(y + z * 2, x + 1, y + z))


def main():
    x, y, z = map(int, input().split())
    print(answer(x, y, z))


def __starting_point():
    main()
__starting_point()
