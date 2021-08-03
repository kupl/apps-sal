s = input()
str2 = s[0: (len(s) - 1) // 2]
str3 = s[(len(s) + 3) // 2: len(s) - 1]
if s == ''.join(list(reversed(s))) \
        and str2 == ''.join(list(reversed(str2))) \
        and str3 == ''.join(list(reversed(str3))):
    print('Yes')
else:
    print('No')
