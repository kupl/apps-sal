S = input()
T = input()
if sorted(S) < sorted(T, reverse=True):
    print('Yes')
else:
    print('No')
