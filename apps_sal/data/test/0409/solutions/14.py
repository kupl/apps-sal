s = input()
pos = -1
pos1 = -1
for i in range(len(s) - 1):
    if s[i] == 'A' and s[i + 1] == 'B':
        pos = i
        break
for i in range(len(s) - 1, 0, -1):
    if s[i] == 'A' and s[i - 1] == 'B':
        pos1 = i - 1
        break
pos2 = -1
pos3 = -1
for i in range(len(s) - 1):
    if s[i] == 'B' and s[i + 1] == 'A':
        pos2 = i
        break
for i in range(len(s) - 1, 0, -1):
    if s[i] == 'B' and s[i - 1] == 'A':
        pos3 = i - 1
        break
if pos == -1 or pos1 == -1:
    flag = False
else:
    if abs(pos - pos1) > 1:
        flag = True
    else:
        flag = False
if flag:
    print('YES')
else:
    if pos2 == -1 or pos3 == -1:
        print('NO')
    else:
        if abs(pos2 - pos3) > 1:
            print('YES')
        else:
            print('NO')
