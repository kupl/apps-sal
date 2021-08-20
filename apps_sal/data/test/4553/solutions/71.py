(a, b) = map(int, input().split())
s = input()
if '-' in s and s.count('-') == 1:
    s = s.split('-')
    if len(s[0]) == a and len(s[1]) == b:
        print('Yes')
    else:
        print('No')
else:
    print('No')
