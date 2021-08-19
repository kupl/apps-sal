def main():
    N = int(input())
    L = input()
    A = [None] * (N + 1)
    for (a0, a1) in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        A[0] = a0
        A[1] = a1
        for i in range(2, N + 1):
            a = A[i - 1]
            s = 0 if L[i - 1] == 'o' else 1
            A[i] = A[i - 2] ^ (a ^ s)
        am = A[1] ^ (A[0] ^ (L[0] == 'x'))
        if A[0] == A[N] and am == A[N - 1]:
            exists = True
            break
    else:
        exists = False
    if exists:
        ans = []
        for i in range(N):
            c = 'W' if A[i] else 'S'
            ans.append(c)
        print(''.join(ans))
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
