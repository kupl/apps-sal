s = list(input())
flag = [0] * 26
for i in range(len(s)):
    flag[ord(s[i]) - 97] = 1
c = 0
for i in range(26):
    if flag[i] == 0:
        print(chr(i + 97))
        break
    else:
        c += 1
if c == 26:
    print('None')
