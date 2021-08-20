s = input().strip()
su = 0
for k in range(len(s)):
    if s[k] == 'a':
        su += 1
mm = (len(s) - su) // 2 + su
ss = s[:mm]
s1 = ''
for k in range(mm):
    if s[k] != 'a':
        s1 = s1 + s[k]
sf = ss + s1
if len(s) != len(sf):
    print(':(')
else:
    for k in range(len(s)):
        if s[k] != sf[k]:
            print(':(')
            break
    else:
        print(ss)
