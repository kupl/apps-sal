s = input()
u = 0
for i in range(int(input())):
    l = input()
    u = 0
    if len(l) == len(s):
        for j in range(len(l)):
            if l[j].lower() == s[j].lower() or (l[j] == '0' and s[j].lower() == 'o') or (s[j] == '0' and l[j].lower() == 'o') or (l[j] == '1' and (s[j].lower() == 'l' or s[j].upper() == 'I')) or (l[j].lower() == 'l' and (s[j] == '1' or s[j].upper() == 'I')) or (l[j].upper() == 'I' and (s[j].lower() == 'l' or s[j] == '1')):
                u += 1
            else:
                break
    if u == len(s):
        break
if u == len(s):
    print('No')
else:
    print('Yes')
