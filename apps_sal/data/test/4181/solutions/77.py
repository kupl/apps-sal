def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        if A[i] >= B[i]:
            ans += B[i]
        else:
            ans += A[i]
            remain = B[i] - A[i]
            if A[i + 1] >= remain:
                ans += remain
                A[i + 1] -= remain
            else:
                ans += A[i + 1]
                A[i + 1] = 0
    print(ans)


def __starting_point():
    main()


__starting_point()
