import sys


def resolve(in_):
    N = int(next(in_))
    S = next(in_).strip()
    if N % 2:
        return 'No'
    n2 = N // 2
    return 'Yes' if S[:n2] == S[n2:] else 'No'


def main():
    answer = resolve(sys.stdin)
    print(answer)


def __starting_point():
    main()


__starting_point()
