def resolve():
    (N, X) = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        diff = max(A[i - 1] + A[i] - X, 0)
        ans += diff
        A[i] = max(A[i] - diff, 0)
    print(ans)


def __starting_point():
    resolve()


__starting_point()
