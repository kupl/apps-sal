s = sorted(input())
t = sorted(input(),reverse = True)
flag1 = True
flag2 = False
if len(s) < len(t):
    for i in range(len(s)):
        if s[i] != t[i]:
            flag1 = False
            break
else:
    flag1 = False
for i in range(min(len(s), len(t))):
    if s[i] < t[i]:
        flag2 = True
        break
    elif s[i] > t[i]:
        break
if flag1 or flag2:
    print('Yes')
else:
    print('No')

