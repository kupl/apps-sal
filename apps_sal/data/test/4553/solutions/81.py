a, b = map(int, input().split())
s = input().rstrip().split('-')
if len(s) == 2 and len(s[0]) == a and len(s[1]) == b:
    print('Yes')
else:
    print('No')
