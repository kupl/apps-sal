
def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    B = [a - i for i, a in enumerate(A, 1)]
    B.sort()
    x = B[N // 2]

    ans = 0
    for b in B:
        ans += abs(x - b)

    print(ans)


def __starting_point():
    resolve()


__starting_point()
