from collections import defaultdict


def main():
    INF = float('inf')
    (N, *A) = map(int, open(0).read().split())
    dp_in = defaultdict(lambda: -INF)
    dp_out = defaultdict(lambda: -INF)
    dp_out[0, 0] = 0
    for (i, a) in enumerate(A, 1):
        p = i // 2
        for j in [p - 1, p, p + 1]:
            dp_in[i, j] = a + dp_out[i - 1, j - 1]
            dp_out[i, j] = max(dp_in[i - 1, j], dp_out[i - 1, j])
    print(max(dp_in[N, N // 2], dp_out[N, N // 2]))


main()
