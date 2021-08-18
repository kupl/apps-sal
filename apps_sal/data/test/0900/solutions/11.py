

def solve():
    S = input()
    mod = 10 ** 9 + 7

    '''
    桁数毎・余りの数字ごとのdpを作成するにあたり、mapを作る.
    たとえば新しい数字Yは前の数字Xの右側に新たに桁を作って
        Y = X(前の数字) * 10 + i(0 <= i <= 9)
    と表せる.
    この Y の余りは、
        Y % 13 = ((X % 13) * 10 + i) % 13
    と表せるので、10 * 13 のマップであらかじめ計算しておくことができる.
    このマップを以下で作っている.
        modmap[新しい桁の数字i][新しい余り(Y % 13 = k)] = 前の数字の時の余り(X % 13 = j)
    '''
    modmap = []
    for i in range(10):
        modmap.append([0] * 13)
        for j in range(13):
            k = (j * 10 + i) % 13
            modmap[i][k] = j

    dp = [1] + [0] * 12
    for s in S:
        if s == '?':
            dp = [sum(dp[l] for l in modlist) % mod for modlist in zip(*modmap)]
        else:
            modlist = modmap[int(s)]
            dp = [dp[modlist[l]] % mod for l in range(13)]

    print((dp[5]))


def __starting_point():
    solve()


__starting_point()
