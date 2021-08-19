import sys


def resolve(in_):
    S = next(in_).strip()
    ans = 0
    for (a, b) in zip(S[:len(S) // 2], reversed(S)):
        if a != b:
            ans += 1
    return ans


def main():
    answer = resolve(sys.stdin)
    print(answer)


def __starting_point():
    main()


__starting_point()
