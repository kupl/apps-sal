def __starting_point():
    N = int(input())
    A = list(map(int, input().lstrip().split(' ')))
    cumA = [A[0]]
    for i in range(1, N):
        cumA.append(cumA[-1] + A[i])
    count = 0
    for i in range(N - 1):
        count += A[i] * (cumA[N - 1] - cumA[i])
    print(count % (10 ** 9 + 7))


__starting_point()
