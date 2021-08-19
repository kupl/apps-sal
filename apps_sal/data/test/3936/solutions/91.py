def resolve():
    N = int(input())
    S1 = list(input())
    S2 = list(input())
    mod = 10 ** 9 + 7
    if S1[0] == S2[0]:
        ans = 3
        now = 0
        ct = 1
    else:
        ans = 6
        now = 1
        ct = 2
    while ct < N:
        if S1[ct] == S2[ct]:
            if now == 0:
                ans *= 2
                ans %= mod
            else:
                pass
            now = 0
            ct += 1
        else:
            if now == 0:
                ans *= 2
                ans %= mod
            else:
                ans *= 3
                ans %= mod
            now = 1
            ct += 2
    print(ans)


resolve()
