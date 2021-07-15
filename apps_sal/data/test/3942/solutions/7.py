#!/usr/bin/env python3

s = input()
count = 0
res = []
last = s.rfind("#")

for i, c in enumerate(s):
    if c == '(':
        count += 1
    elif c == ')':
        count -= 1
    else:
        if i < last:
            res.append(1)
            count -= 1
        else:
            num = max(1, 1 + s.count("(") - s.count("#") - s.count(")"))
            res.append(num)
            count -= num
    if count < 0:
        res = []
        print(-1)
        break
for i in res:
    print(i)

