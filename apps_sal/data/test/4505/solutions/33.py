S = input()
S1 = len(set(S))

if ('a' and 'b' and 'c' in S) and (S1 == 3):
    print('Yes')
else:
    print('No')
