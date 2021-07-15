S = input()
if 'L' in S[::2]:
    print('No')
elif 'R' in S[1::2]:
    print('No')
else:
    print('Yes')
