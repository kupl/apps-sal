S = input()
even = S[1::2]
odd = S[::2]
if 'R' not in even and 'L' not in odd:
    print('Yes')
else:
    print('No')
