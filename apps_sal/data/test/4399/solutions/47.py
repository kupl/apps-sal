S = list(input())
S_sorted = ''.join(sorted(S))
if S_sorted == 'AAA' or S_sorted == 'BBB':
    print('No')
else:
    print('Yes')
