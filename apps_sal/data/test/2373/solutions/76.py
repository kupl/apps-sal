def main():
    N = int(input())
    P = list(map(int, input().split()))
    cnt = 0
    for i in range(N - 1):
        if P[i] == i + 1:
            cnt += 1
            P[i + 1], P[i] = P[i], P[i + 1]
    if P[N - 1] == N:
        cnt += 1
    print(cnt)


def __starting_point():
    main()


__starting_point()
