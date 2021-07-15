from numpy import zeros, maximum, array

def main():
    N, T, *AB = array(open(0).read().split(), int)

    dp = zeros(6010, int)
    for w, v in sorted(zip(*[iter(AB)] * 2)):
        dp[w:T + w] = maximum(dp[w:T + w], dp[:T] + v)

    print(dp.max())

main()
