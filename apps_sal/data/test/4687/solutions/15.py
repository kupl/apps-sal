def main():
    (N, K) = list(map(int, input().split()))
    lis = []
    for i in range(N):
        (a, b) = list(map(int, input().split()))
        lis.append((a, b))
    lis = sorted(lis)
    for i in range(N):
        K -= lis[i][1]
        if K <= 0:
            print(lis[i][0])
            break


def __starting_point():
    main()


__starting_point()
