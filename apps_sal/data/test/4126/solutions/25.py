s = input()
l = len(s)
okey = 1
ll = l // 2
for i in range(0, l // 2):
    if s[i] != s[l - i - 1]:
        okey = 0
        break
if okey == 1:
    for i in range(0, ll // 2):
        if s[i] != s[ll - i - 1]:
            okey = 0
            break
if okey == 1:
    for i in range(ll + 1, ll + ll // 2):
        if s[i] != s[l - i - 1]:
            okey = 0
            break
if okey == 1:
    print('Yes')
else:
    print('No')
