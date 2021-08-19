S = input()
if len(S) % 2 == 0 and S[0] == S[len(S) - 1]:
    print('First')
elif len(S) % 2 == 0 and S[0] != S[len(S) - 1]:
    print('Second')
elif len(S) % 2 != 0 and S[0] == S[len(S) - 1]:
    print('Second')
else:
    print('First')
