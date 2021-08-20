(N, K) = map(int, input().split())


def ans156(N: int, K: int):
    length = 1
    while True:
        if N < K:
            break
        N = int(N / K)
        length += 1
    return length


print(ans156(N, K))
