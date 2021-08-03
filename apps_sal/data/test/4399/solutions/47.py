# AAA or BBB ならNo

S = list(input())

S_sorted = ''.join(sorted(S))
# print(S_sorted)

if S_sorted == 'AAA' or S_sorted == 'BBB':
    print('No')
else:
    print('Yes')
