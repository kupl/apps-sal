import sys
S = input()
N = len(S)
if N % 2 != 0:
    if S[0] == S[N - 1]:
        print('Second')
    else:
        print("First")
else:
    if S[0] == S[N - 1]:
        print('First')
    else:
        print('Second')
