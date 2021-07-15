def main():
    N, K = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]

    f, b = 0, 0
    ans = 0
    v = A[0]
    while(f < N):
        if v < K:
            b += 1
            if b == N:
                break
            else:
                v += A[b]
        else:
            ans += N - b
            v -= A[f]
            f += 1
    print(ans)


def __starting_point():
    main()

__starting_point()
