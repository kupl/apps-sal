S = input()

if S[0] == S[-1]:
    if len(S) % 2 == 1:
        print('Second')
    else:
        print('First')
else:
    if len(S) % 2 == 0:
        print('Second')
    else:
        print('First')
