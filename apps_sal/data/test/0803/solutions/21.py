#!/usr/local/bin/python3

n = list(map(int, input()))
a = list(input())
i_x = a.count('x')
i_X = a.count('X')
result = int(abs(i_x - i_X) / 2)
print(result)
cnt = 0
if i_x > i_X:
    flag = 1
elif i_x < i_X:
    flag = 0
else:
    flag = -1
for i in range(len(a)):
    if flag == -1:
        break
    if a[i] == 'x':
        if flag == 1:
            a[i] = 'X'
            cnt += 1
    else:
        if flag == 0:
            a[i] = 'x'
            cnt += 1
    if cnt == result:
        break
print("".join(a))
