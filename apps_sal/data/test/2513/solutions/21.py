def main():
    # import sys
    # readline = sys.stdin.buffer.readline
    # readlines = sys.stdin.buffer.readlines
    N = int(input())
    L = input()

    A = [None] * (N + 2)
    for a0, a1 in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        A[0] = a0
        A[1] = a1
        for i in range(2, N + 1):
            a = A[i - 1]
            s = (L[i - 1] == 'x')
            A[i] = A[i - 2] ^ (a ^ s)
        A[N + 1] = A[N - 1] ^ (A[N] ^ (L[0] == 'x'))
        if A[0] == A[N] and A[1] == A[N + 1]:
            exists = True
            break
    else:
        exists = False

    if exists:
        ans = []
        for i in range(N):
            c = 'W' if A[i] else 'S'
            ans.append(c)
        print((''.join(ans)))
    else:
        print((-1))


def __starting_point():
    main()

__starting_point()
