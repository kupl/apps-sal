def main():
    n = input()
    non_zero = int(input())
    length = len(n)
    dp = [[[0, 0] for _ in range(non_zero + 1)] for _ in range(length + 1)]
    dp[0][0][0] = 1
    for i in range(length):
        for j in range(non_zero + 1):
            for k in range(2):
                now_digit = int(n[i])
                for next_d in range(10):
                    new_i = i + 1
                    new_j = j
                    new_k = k
                    if next_d > 0:
                        new_j += 1
                    if new_j > non_zero:
                        continue
                    if k == 0:
                        if next_d > now_digit:
                            continue
                        elif next_d < now_digit:
                            new_k = 1
                    dp[new_i][new_j][new_k] += dp[i][j][k]
    print(sum(dp[length][non_zero]))


def __starting_point():
    main()


__starting_point()
