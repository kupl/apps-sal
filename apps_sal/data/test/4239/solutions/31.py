import numpy as np

N = int(input())


# @njit
def main(n):
    dp = []
    for i in range(10**5 + 1):
        dp.append(i)
    dp = np.array(dp)
    powers = [1]
    i = 1
    while True:
        if 6**i > 10**5:
            break
        powers.append(6**i)
        if 9**i <= 10**5:
            powers.append(9**i)
        i += 1
    powers.sort()
    for i in range(1, 10**5 + 1):
        for j in range(len(powers)):
            if powers[j] > i:
                break
            dp[i] = min(dp[i], dp[i - powers[j]] + 1)

    print(dp[n])


def __starting_point():
    main(N)


__starting_point()
