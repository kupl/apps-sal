import sys
import itertools


def resolve(in_):
    N = int(next(in_))
    (S, T) = next(in_).strip().split()
    ans = itertools.chain.from_iterable(list(zip(S, T)))
    return ''.join(ans)


def main():
    answer = resolve(sys.stdin)
    print(answer)


def __starting_point():
    main()


__starting_point()
