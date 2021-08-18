def main():
    N = int(input())
    S = []
    S.append(input())
    S.append(input())
    MOD = 10**9 + 7
    ans = 1
    pre_mino_flag = -1
    pass_flag = False
    if S[0][0] == S[1][0]:
        ans *= 3
        pre_mino_flag = 0
    else:
        ans *= 6
        pre_mino_flag = 1
        pass_flag = True

    for i in range(1, N):
        if pass_flag:
            pass_flag = False
            continue

        if S[0][i] == S[1][i]:
            if pre_mino_flag == 0:
                ans *= 2
                ans %= MOD
            else:
                pass
            pre_mino_flag = 0
        else:
            pass_flag = True
            if pre_mino_flag == 0:
                ans *= 2
                ans %= MOD
            else:
                ans *= 3
                ans %= MOD
            pre_mino_flag = 1

    print(ans)


def __starting_point():
    main()


__starting_point()
