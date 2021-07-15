def answer(n: int, s: str) -> str:
    result = []
    A = ord('A')
    for i in s:
        result.append(chr(A + (ord(i) - A + n) % 26))

    return ''.join(result)


def main():
    n = int(input())
    s = input()
    print((answer(n, s)))


def __starting_point():
    main()

__starting_point()
