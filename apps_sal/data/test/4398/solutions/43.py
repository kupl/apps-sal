def answer(n: int, s: str, t: str) -> str:
    new_str = ''
    for i in range(n):
        new_str += f'{s[i]}{t[i]}'
    return new_str


def main():
    n = int(input())
    (s, t) = input().split()
    print(answer(n, s, t))


def __starting_point():
    main()


__starting_point()
