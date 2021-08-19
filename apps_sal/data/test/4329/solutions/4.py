S = input()
T = input()
if len(T) == len(S) + 1 and T == S + T[len(T) - 1]:
    print('Yes')
else:
    print('No')
