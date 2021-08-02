S = input()
size = len(S)


def palin(S, size):
    for i in range(size // 2):
        if S[i] != S[-1 - i]:
            return False
    return True


if palin(S, size) == True:
    L = S[:size // 2]
    R = S[size // 2 + 2:]
    if palin(L, size // 2) & palin(L, size // 2):
        print('Yes')
    else:
        print('No')
else:
    print('No')
