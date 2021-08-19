S = str(input())
odd = list(S[0::2])
even = list(S[1::2])
if all([n == 'R' or n == 'U' or n == 'D' for n in odd]) and all([n == 'L' or n == 'U' or n == 'D' for n in even]):
    print('Yes')
else:
    print('No')
