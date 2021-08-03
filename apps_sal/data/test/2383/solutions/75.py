import sys


def resolve(in_):
    N = int(next(in_))
    A = tuple(map(int, next(in_).split()))

    ans = 0
    x = 1
    for a in A:
        if x == a:
            x += 1
        else:
            ans += 1

    if N == ans:
        ans = -1
    return ans


def main():
    answer = resolve(sys.stdin)
    print(answer)


def __starting_point():
    main()


__starting_point()
