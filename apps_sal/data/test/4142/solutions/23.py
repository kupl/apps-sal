S = input()

a = {'R', 'U', 'D'}
b = {'L', 'U', 'D'}
Odd = set(S[0::2])
Even = set(S[1::2])

if Even <= b and Odd <= a:
    print('Yes')
else:
    print('No')
