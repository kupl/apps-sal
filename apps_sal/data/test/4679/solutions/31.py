Sa = input()
Sb = input()
Sc = input()
S_dic = {0: 'a', 1: 'b', 2: 'c'}
S_dic_L = {0: 'A', 1: 'B', 2: 'C'}
S_dic_inv = {'a': 0, 'b': 1, 'c': 2}

S = [Sa, Sb, Sc]


def find_game(x):
    if S[x] == '':
        print((S_dic_L[x]))
        return

    else:
        p = S[x][0]
        S[x] = S[x][1:]

        find_game(S_dic_inv[p])


find_game(0)
