# coding: utf-8


def main():
    N, K = list(map(int, input().split()))
    ans = 0.0
    for i in range(1, N + 1):
        j, k = i, 0
        while j < K:
            j *= 2
            k += 1
        ans += pow(0.5, k) / N

    print(ans)

def __starting_point():
    main()

__starting_point()
