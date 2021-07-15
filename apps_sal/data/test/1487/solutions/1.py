s1 = input()
s2 = input()
cnt = 0
s = ''
for i in range(len(s1)):
    if s1[i] != s2[i]:
        if cnt % 2 == 0:
            s += s1[i]
        else:
            s += s2[i]
        cnt += 1
    else:
        s += s1[i]
if cnt % 2 == 0:
    print(s)
else:
    print('impossible')

