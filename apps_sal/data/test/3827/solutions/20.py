# -*- coding: UTF-8 -*-

s = input()
status = ['a', 'b', 'c']
count = [0, 0, 0]
p = 0
flag = True

for c in s:
    while p < 3 and c != status[p]:
        p += 1
    if p >= 3:
        flag = False
        break
    count[p] += 1

if count[0] == 0 or count[1] == 0 or count[2] == 0:
    flag = False
if count[0] != count[2] and count[1] != count[2]:
    flag = False
if flag:
    print('YES')
else:
    print('NO')
