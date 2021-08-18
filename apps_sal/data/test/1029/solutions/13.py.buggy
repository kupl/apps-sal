s = input() + '#'
if len(s) == 2:
    print(1)
    return
elif '0' not in s:
    if int(s[0]) < int(s[1]):
        print(len(s) - 2)
    else:
        print(len(s) - 1)
else:
    c = 0
    ind = -1
    ans = 0
    zer = s.count('0')
    for i in range(len(s)):
        if s[i] == '0':
            c += 1
        else:
            if i - c - 1 < c + 1:
                ans = i
            elif c + 1 == i - c - 1 and s[:i - c - 1] < s[i - c - 1:i]:
                ans = i
            c = 0
    a = s[:ans].count('0')
    zer -= a
    print(len(s) - ans - zer)
