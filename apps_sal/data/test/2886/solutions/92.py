import re
s = input()
set_s = set(s)
flag = 0
if len(s) == 2:
    if s[0] == s[1]:
        print(1, 2)
        flag = 1
    else:
        flag = 1
        print(-1, -1)
for x in set_s:
    regex1 = re.compile(x + x + '\\w')
    regex2 = re.compile(x + '\\w' + x)
    mo1 = regex1.search(s)
    mo2 = regex2.search(s)
    if mo1:
        print(mo1.start() + 1, mo1.end())
        flag = 1
        break
    elif mo2:
        print(mo2.start() + 1, mo2.end())
        flag = 1
        break
if not flag:
    print(-1, -1)
