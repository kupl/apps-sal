S = input()
T = input()

if S == T[:-1] and len(T[-1:]) == 1:
    print('Yes')
else:
    print('No')
