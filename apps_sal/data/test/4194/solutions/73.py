def __starting_point():
    (N, M) = list(map(int, input().split()))
    li = list(map(int, input().split()))
    if N >= sum(li):
        print(N - sum(li))
    else:
        print('-1')


__starting_point()
