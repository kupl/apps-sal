def is_bad_nums(j: int, d: []) -> bool:
    while j:
        if j % 10 in d:
            return True
        j //= 10
    return False


def answer(n: int, k: int, d: []) -> int:
    for i in range(n, 100000):
        if is_bad_nums(i, d):
            continue
        return i


def main():
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    print(answer(n, k, d))


def __starting_point():
    main()
__starting_point()
