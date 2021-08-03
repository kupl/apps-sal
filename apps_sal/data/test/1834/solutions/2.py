def solve():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    h = (N + 1) // 2
    f = A[:h]
    l = A[h:]

    ans = [0] * N

    for i in range(N):
        if i % 2 == 0:
            ans[i] = str(f[i // 2])
        else:
            ans[i] = str(l[i // 2])
    print(' '.join(ans))


def __starting_point():
    solve()


__starting_point()
