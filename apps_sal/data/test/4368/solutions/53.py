N, K = map(int, input().split())


def ans156(N: int, K: int):
    length = 1  # 0桁はないため、1からスタート
    while True:
        if N < K:
            break
        N = int(N / K)  # 割り切れるごとに1桁ずつ増えていく。
        length += 1
    return length


print(ans156(N, K))
