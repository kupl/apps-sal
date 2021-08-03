
def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = [0] * N
    ans[0] = sum(A)

    for i in range(1, N, 2):
        ans[0] -= 2 * A[i]

    for i in range(N - 1):
        ans[i + 1] = 2 * A[i] - ans[i]

    print(*ans)


def __starting_point():
    resolve()


__starting_point()
