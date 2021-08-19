(s, t) = (sorted(input()), sorted(input())[::-1])
if ''.join(s) < ''.join(t):
    print('Yes')
else:
    print('No')
