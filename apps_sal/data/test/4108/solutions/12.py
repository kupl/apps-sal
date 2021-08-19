def solve(S, T):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    N = len(S)
    S_same = [[] for _ in range(N)]
    S_alphabet = {s: [] for s in alp}
    T_same = [[] for _ in range(N)]
    T_alphabet = {s: [] for s in alp}
    for i in range(N):
        S_alphabet[S[i]].append(i)
        T_alphabet[T[i]].append(i)
    for s in alp:
        stmp = S_alphabet[s]
        ttmp = T_alphabet[s]
        if len(stmp) > 0:
            S_same[stmp[0]] = stmp.copy()
        if len(ttmp) > 0:
            T_same[ttmp[0]] = ttmp.copy()
    for i in range(N):
        if len(S_same[i]) > 1:
            for ss in S_same[i][1:]:
                if T[S_same[i][0]] != T[ss]:
                    print('No')
                    return
        if len(T_same[i]) > 1:
            for tt in T_same[i][1:]:
                if S[T_same[i][0]] != S[tt]:
                    print('No')
                    return
    print('Yes')


def __starting_point():
    S = input()
    T = input()
    solve(S, T)


__starting_point()
