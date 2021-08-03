S = input()
N = len(S)
if N % 2 == 0:
    if S[0] == S[-1]:
        print('First')
    else:
        print('Second')
else:
    if S[0] == S[-1]:
        print('Second')
    else:
        print('First')
