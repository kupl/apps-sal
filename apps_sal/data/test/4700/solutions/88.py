
def __starting_point():
    N, M = list(map(int, input().split()))
    Hli = list(map(int, input().split()))

    ans = [0] * N

    for i in range(M):
        A, B = list(map(int, input().split()))

        if Hli[A - 1] < Hli[B - 1]:
            ans[A - 1] += 1

        elif Hli[A - 1] == Hli[B - 1]:
            ans[A - 1] += 1
            ans[B - 1] += 1

        else:
            ans[B - 1] += 1

    print((ans.count(0)))


__starting_point()
