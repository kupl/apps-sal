def solve(N, a):
    print(sum([ai - 1 for ai in a]))


def __starting_point():
    N = int(input())
    a = [int(i) for i in input().split()]
    solve(N, a)


__starting_point()
