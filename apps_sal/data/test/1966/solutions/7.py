from itertools import permutations


def main():
    n = int(input())
    cb0 = [list(map(int, input())) for _ in range(n)]
    _ = input()
    cb1 = [list(map(int, input())) for _ in range(n)]
    _ = input()
    cb2 = [list(map(int, input())) for _ in range(n)]
    _ = input()
    cb3 = [list(map(int, input())) for _ in range(n)]
    print(solve(n, [cb0, cb1, cb2, cb3]))


def solve(n, cbs):
    return min(cost(n, p) for p in permutations(cbs))


def cost(n, p):
    n2 = 2 * n
    p2 = [p[:2], p[2:]]
    cost1 = sum(1 for i in range(n2) for j in range(n2) if p2[i // n][j // n][i % n][j % n] == (i + j) % 2)
    cost2 = sum(1 for i in range(n2) for j in range(n2) if p2[i // n][j // n][i % n][j % n] == (i + j + 1) % 2)
    return min(cost1, cost2)


main()
