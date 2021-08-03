
def main():
    with open(0) as f:
        S, T = f.read().split()
    for i in reversed(range(len(S) - len(T) + 1)):
        for j in reversed(range(len(T))):
            if S[i + j] == T[j] or S[i + j] == '?':
                continue
            else:
                break
        else:
            S = S[:i] + T + S[i + len(T):]
            S = S.replace('?', 'a')
            print(S)
            break
    else:
        print('UNRESTORABLE')


main()
