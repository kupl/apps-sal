s = input()
cnt_up = 0
cnt = 0
if s[0] == 'A':
    for i in range(len(s)):
        if s[i].isupper():
            cnt_up += 1
        if i > 1 and i < len(s) - 1 and (s[i] == 'C'):
            cnt += 1
if cnt_up == 2 and cnt == 1:
    print('AC')
else:
    print('WA')
