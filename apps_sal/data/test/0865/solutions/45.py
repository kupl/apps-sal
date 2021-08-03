from numpy import zeros, maximum, int32


def main():
    N, T, *AB = list(map(int, open(0).read().split()))

    dp = zeros(6010, int32)
    for w, v in sorted(zip(*[iter(AB)] * 2)):
        dp[w:T + w] = maximum(dp[w:T + w], dp[:T] + v)

    print((dp.max()))


main()
