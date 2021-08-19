s = input()
ss = []
i = 0
while i < len(s):
    if s[i].isdigit() == True:
        i += 1
    elif s[i] == '+' and s[i - 1].isdigit() == True and (i != 0):
        for j in range(i + 1, len(s)):
            if s[j] == '-':
                break
        ss.append(int(s[i - 1]) * s[i + 1:j])
        i = j + 1
    elif s[i] == '+' and s[i - 1].isdigit() == False and (i != 0):
        for j in range(i + 1, len(s)):
            if s[j] == '-':
                break
        ss.append(s[i + 1:j])
        i = j + 1
    elif s[i] == '+' and i == 1:
        for j in range(i + 1, len(s)):
            if s[j] == '-':
                break
        ss.append(s[i + 1:j])
        i = j + 1
    else:
        ss.append(s[i])
        i += 1
ss = ''.join(ss)
if ss == ss[::-1]:
    print('Return')
else:
    print('Continue')
