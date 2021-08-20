S = list(input())
N = len(S)
A = N % 2
B = (S[0] == S[-1]) * 1
if A == 1 and B == 1:
    print('Second')
elif A == 1 and B == 0:
    print('First')
elif A == 0 and B == 1:
    print('First')
elif A == 0 and B == 0:
    print('Second')
