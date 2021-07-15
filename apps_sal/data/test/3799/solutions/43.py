S = input()
if (S[0] == S[-1]) ^ (len(S) % 2):
    print('First')
else:
    print('Second')

