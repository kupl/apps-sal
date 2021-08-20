def solve(N, K):
    div0 = N // K
    divh = (N + K // 2) // K if K % 2 == 0 else 0
    import math
    print(div0 ** 3 + divh ** 3)


def __starting_point():
    (N, K) = list(map(int, input().split()))
    solve(N, K)


__starting_point()
