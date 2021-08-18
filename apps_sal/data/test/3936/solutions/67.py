
def resolve():
    MOD = 10 ** 9 + 7
    N = int(input())
    S = input()
    T = input()

    i = 0
    ans = 0

    flag = 1
    if S[i] == T[i]:
        ans = 3
        i += 1
        flag = 1
    else:
        ans = 6
        i += 2
        flag = 2

    while i < N:
        if S[i] == T[i]:
            if flag == 1:
                ans *= 2
                ans %= MOD
            i += 1
            flag = 1
        else:
            if flag == 1:
                ans *= 2
                ans %= MOD
            else:
                ans *= 3
                ans %= MOD
            i += 2
            flag = 2

    print(ans)


def __starting_point():
    resolve()


__starting_point()
