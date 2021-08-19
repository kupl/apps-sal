s = input()
s1 = s[:2]
s2 = s[2:]
if s[0] == s[1] and s[0] == s[2] and (s[0] == s[3]):
    print('No')
elif s1[0] == s1[1]:
    if s2[0] == s2[1]:
        print('Yes')
    else:
        print('No')
elif s1[0] == s2[1]:
    if s1[1] == s2[0]:
        print('Yes')
    else:
        print('No')
elif s1[1] == s2[1]:
    if s1[0] == s2[0]:
        print('Yes')
    else:
        print('No')
else:
    print('No')
