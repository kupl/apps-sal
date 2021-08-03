def main():
    X, Y, A, B, C = list(map(int, input().split()))
    *P, = list(map(int, input().split()))
    *Q, = list(map(int, input().split()))
    *R, = list(map(int, input().split()))

    P.sort(reverse=True)
    Q.sort(reverse=True)

    ans = sum(sorted(P[:X] + Q[:Y] + R, reverse=True)[:X + Y])
    print(ans)


def __starting_point():
    main()


__starting_point()
