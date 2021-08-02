s = input()

flag = True

if s[0] != 'A':
    flag = False

res = 0
for i in range(2, len(s) - 1):
    if s[i] == 'C':
        res += 1

    if res >= 2:
        flag = False
        break
if res == 0:
    flag = False

res = 0
for i in range(0, len(s)):
    if s[i].isupper():
        res += 1

    if res > 2:
        flag = False
        break

if flag:
    print('AC')
else:
    print('WA')
