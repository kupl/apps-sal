def resolve():
    N = int(input())
    S1 = list(input())
    S2 = list(input())
    mod = 10**9+7
    if S1[0] == S2[0]:
        ans = 3
        now = 0 #0 ==縦
        ct = 1
    else:
        ans = 6
        now = 1 #1 横
        ct = 2

    while ct < N:
        if S1[ct] == S2[ct]:    #次が縦
            if now == 0:        #前が縦
                ans *= 2
                ans %= mod
            else:               #前が横
                pass
            now = 0
            ct += 1
        else:                   #次が横
            if now == 0:        #前が縦
                ans *= 2
                ans %= mod
            else:               #前が横
                ans *= 3
                ans %= mod
            now = 1
            ct += 2

    print(ans)
resolve()
