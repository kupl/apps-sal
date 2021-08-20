S = input()
T = input()
if len(S) + 1 == len(T) and S + T[-1] == T:
    print('Yes')
else:
    print('No')
