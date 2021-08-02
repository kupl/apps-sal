import itertools


def main():
    N, M = list(map(int, input().split(' ')))
    cakes = [list(map(int, input().split(' '))) for _ in range(N)]
    ans = 0
    for sign in itertools.product([-1, 1], repeat=3):
        scores = [sum([s * c for s, c in zip(sign, cake)]) for cake in cakes]
        scores.sort(reverse=True)
        ans = max([ans, sum(scores[:M])])
    print(ans)


def __starting_point():
    main()


__starting_point()
