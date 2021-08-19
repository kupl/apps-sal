def registration():
    S = input()
    T = input()
    for (i, j) in enumerate(S):
        if T[i] != j:
            break
    else:
        print('Yes')
        return
    print('No')


registration()
