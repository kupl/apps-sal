S = input()
odd_step = list(S[0::2])
even_step = list(S[1::2])
if 'R' not in even_step and 'L' not in odd_step:
    print('Yes')
else:
    print('No')
