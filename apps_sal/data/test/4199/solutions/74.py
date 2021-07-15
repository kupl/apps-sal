
def answer(n: int, k: int, h: []) -> int:
    return len(list(i for i in h if k <= i))


def main():
    n, k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    print((answer(n, k, h)))


def __starting_point():
    main()

__starting_point()
