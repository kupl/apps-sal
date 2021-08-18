S = input()

n1 = len(S)
n2 = len(set(S))

if n1 == n2:
    print('yes')
else:
    print('no')
