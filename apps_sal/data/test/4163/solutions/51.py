# -*- coding: utf-8 -*-
d = []
num = int(input())
for i in range(num):
    s = input()
    d.append(s.split())

try_count = 0
zorome_count = 0
temp = 0
result = "No"
for i in range(num):
    if d[i][0] == d[i][1]:
        zorome_count += 1
        if i-temp == 1 and zorome_count >= 3:
            result = "Yes"
            break
        temp = i
    else:
        zorome_count = 0

print(result)

