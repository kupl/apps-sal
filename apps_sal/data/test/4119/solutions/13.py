def solve(N, M, Xi):
    lengthes = []
    Xi.sort()
    for i in range(1, M):
        lengthes.append(abs(Xi[i - 1] - Xi[i]))
    lengthes.sort()
    num = N if N < M else M
    print((sum(lengthes[:M - num])))


def __starting_point():
    N, M = list(map(int, input().split()))
    Xi = [int(i) for i in input().split()]
    solve(N, M, Xi)


__starting_point()
