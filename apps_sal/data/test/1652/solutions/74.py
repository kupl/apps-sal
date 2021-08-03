s = input()
s = s[::-1]
tmp = ['dream', 'dreamer', 'erase', 'eraser']
for i in range(4):
    tmp[i] = tmp[i][::-1]
while 1:
    if len(s) >= 5:
        if s[:5] == tmp[0]:
            if len(s) > 5:
                s = s[5:]
            else:
                s = []
            continue
        if s[:5] == tmp[2]:
            if len(s) > 5:
                s = s[5:]
            else:
                s = []
            continue
        if len(s) >= 6:
            if s[:6] == tmp[3]:
                if len(s) > 6:
                    s = s[6:]
                else:
                    s = []
                continue
            if len(s) >= 7:
                if s[:7] == tmp[1]:
                    if len(s) > 7:
                        s = s[7:]
                    else:
                        s = []
                    continue
    break

if s == []:
    print('YES')
else:
    print('NO')
