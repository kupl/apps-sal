def solve(N, Ai, Bi):
    Ci = [0] * (N + 1)
    Di = [0] * (N + 1)
    j = 0
    k = 0
    for i in range(1, N + 1):
        while j < N and Ai[j] <= i:
            j += 1
        Ci[i] = j
        while k < N and Bi[k] <= i:
            k += 1
        Di[i] = k
    for i in range(1, N + 1):
        if Ci[i] - Ci[i - 1] + Di[i] - Di[i - 1] > N:
            print('No')
            return
    x = 0
    for i in range(1, N + 1):
        x = max(x, Ci[i] - Di[i - 1])
    print('Yes')
    print((' '.join([str(Bi[(N - x + i) % N]) for i in range(N)])))


def __starting_point():
    N = int(input())
    Ai = [int(i) for i in input().split()]
    Bi = [int(i) for i in input().split()]
    solve(N, Ai, Bi)


__starting_point()
