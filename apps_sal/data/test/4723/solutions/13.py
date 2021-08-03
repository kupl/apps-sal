s = input()
t = input()

s_length = len(s)
t_length = len(t)

ans = ''
keep = ''
remind = 0
checker = False
for i in range(s_length):
    if (i + t_length) <= s_length:
        check = True
        for j in range(t_length):
            if (s[i + j] != t[j]) & (s[i + j] != '?'):
                check = False
        if check:
            checker = True
            ans = keep + t
            remind = i + t_length
    if s[i] == '?':
        keep += 'a'
    else:
        keep += s[i]
ans = ans + keep[remind:]

if checker:
    print(ans)
else:
    print('UNRESTORABLE')
