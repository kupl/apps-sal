import sys


def solve(N: int, a: "List[int]"):
    a = list(reversed(sorted(a)))
    alice = [a_[1] for a_ in enumerate(a) if a_[0] % 2 == 0]
    bob = [a_[1] for a_ in enumerate(a) if a_[0] % 2 == 1]
    print((sum(alice) - sum(bob)))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    a = [int(next(tokens)) for _ in range(N)]
    solve(N, a)


def __starting_point():
    main()


__starting_point()
