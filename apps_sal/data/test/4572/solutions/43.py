S = list(input())

S.sort()

if S[0] != 'a':
    print('a')
elif S[0] == 'a':
    for i in range(len(S)-1):
        if ord(S[i+1]) - ord(S[i]) == 0 or ord(S[i+1]) - ord(S[i]) == 1:
            pass
        else:
            res = ord(S[i]) + 1
            print((chr(res)))
            return
            
    res = ord(S[-1]) + 1

    if S[0] == 'a' and S[-1] == 'z':
        print('None')
    elif S[0] != 'a':
        print('a')
    else:
        print((chr(res)))

