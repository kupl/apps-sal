s = input()
if '1' not in s:
    print('no')
else:
    i = s.index('1')
    ans = 0
    for j in range(i, len(s)):
        if s[j] == '0':
            ans += 1
    if ans >= 6:
        print('yes')
    else:
        print('no')
