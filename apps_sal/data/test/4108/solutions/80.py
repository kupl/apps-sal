def solve(S, T):
    N = len(S)
    S_check = [0] * N
    T_check = [0] * N
    for i in range(N):
        if S_check[i] == 0:
            S_check[i] = 1
            for j in range(i + 1, N):
                if S[i] == S[j]:
                    S_check[j] = 1
                    if T[i] != T[j]:
                        print('No')
                        return
        if T_check[i] == 0:
            T_check[i] = 1
            for j in range(i + 1, N):
                if T[i] == T[j]:
                    T_check[j] = 1
                    if S[i] != S[j]:
                        print('No')
                        return
    print('Yes')


def __starting_point():
    S = input()
    T = input()
    solve(S, T)


__starting_point()
