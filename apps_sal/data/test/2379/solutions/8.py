def main():
    N, K, C = list(map(int, input().split()))
    S = input()

    i = 0
    c = 0
    p = [-1] * N
    while c < K:
        if S[i] == 'o':
            p[i] = c
            c += 1
            i += C
        i += 1

    i = N - 1
    c = K - 1
    q = [-1] * N
    while c >= 0:
        if S[i] == 'o':
            q[i] = c
            c -= 1
            i -= C
        i -= 1

    for i in range(N):
        if ~p[i] and p[i] == q[i]:
            print((i + 1))


def __starting_point():
    main()

__starting_point()
