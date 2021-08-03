s = sorted(input())
if len(set(s)) == 2 and s[0] == s[1] and s[2] == s[3]:
    print('Yes')
else:
    print('No')
