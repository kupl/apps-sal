def main():

    N = int(input())

    if N == 2 or N == 3: return 1

    cAA = input()
    cAB = input()
    cBA = input()
    cBB = input()

    mod = pow(10, 9) + 7

    v1 = 1
    for i in range(N - 3): v1 = v1 * 2 % mod
    v2 = 1
    dp = [0, 1]
    for i in range(N - 3):
        temp = [0, 0]
        temp[0] = dp[1]
        temp[1] = (dp[0] + dp[1]) % mod
        dp = temp
    v2 = sum(dp) % mod

    # print(v1, v2)

    if cAB == 'B':
        if cBB == 'B': return 1
        else:
            if cBA == 'A':
                return v1
            else:
                return v2
    else:
        if cAA == 'A': return 1
        else:
            if cBA == 'B':
                return v1
            else:
                return v2


def __starting_point():
    print(main())


__starting_point()
