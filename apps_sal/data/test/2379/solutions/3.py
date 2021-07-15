def main():
    N, K, C = map(int, input().split())
    S = input()

    L = [-1] * K  # 0-ind

    i = 0
    cur = 0
    while i < N:
        if S[i] == 'o':
            L[cur] = i
            cur += 1
            if cur == K: break
            i += C
        i += 1

    R = [-1] * K  # 0-ind

    i = N - 1
    cur = K - 1
    while i >= 0:
        if S[i] == 'o':
            R[cur] = i
            cur -= 1
            if cur == -1: break
            i -= C
        i -= 1

    ans = (l + 1 for l, r in zip(L, R) if l == r)  # 1-ind
    print(*ans, sep='\n')


def __starting_point():
    main()

__starting_point()
