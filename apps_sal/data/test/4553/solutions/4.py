(a, b) = map(int, input().split())
s = input()
if len(s.split('-')) == 2 and s[a] == '-':
    print('Yes')
else:
    print('No')
