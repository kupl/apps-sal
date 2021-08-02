s = input()
flag = True
if s[0] != 'A':
    flag = False
if s[1].isupper():
    flag = False
cnt = 0
for i in range(2, len(s) - 1):
    if s[i] == 'C':
        cnt += 1
    elif s[i].isupper():
        flag = False
if s[len(s) - 1].isupper():
    flag = False
if cnt != 1:
    flag = False
if flag:
    print("AC")
else:
    print("WA")
