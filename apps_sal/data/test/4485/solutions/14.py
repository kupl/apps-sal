import sys
input = sys.stdin.readline


def read():
    (N, M) = list(map(int, input().strip().split()))
    AB = []
    for i in range(M):
        (a, b) = list(map(int, input().strip().split()))
        AB.append((a, b))
    return (N, M, AB)


def solve(N, M, AB):
    S = [False for i in range(N + 1)]
    T = [False for i in range(N + 1)]
    for (a, b) in AB:
        if a > b:
            (a, b) = (b, a)
        if a == 1:
            S[b] = True
        elif b == N:
            T[a] = True
    for (s, t) in zip(S, T):
        if s and t:
            return 'POSSIBLE'
    return 'IMPOSSIBLE'


def __starting_point():
    inputs = read()
    print('%s' % solve(*inputs))


__starting_point()
