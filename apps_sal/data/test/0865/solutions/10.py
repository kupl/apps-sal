from numpy import zeros, maximum, array


def main():
    N, T, *AB = list(map(int, open(0).read().split()))

    dp = zeros(T + max(AB[::2]), int)
    for w, v in sorted(zip(*[iter(AB)] * 2)):
        dp[w:T + w] = maximum(dp[w:T + w], dp[:T] + v)

    print((dp.max()))


main()
