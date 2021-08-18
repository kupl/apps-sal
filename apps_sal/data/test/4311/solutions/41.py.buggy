import sys
s = int(input())

cnt = 0

if s == 1 or s == 2:
    print('4')
    return

while s != 4:
    if s % 2 != 0:
        s = 3 * s + 1
        cnt += 1
    elif s % 2 == 0:
        s = s // 2
        cnt += 1

if s == 4:
    print(cnt + 4)
