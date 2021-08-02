S = list(input())
a = S[::2]
b = S[1::2]

if 'L' in a or 'R' in b:
    print('No')

else:
    print('Yes')
