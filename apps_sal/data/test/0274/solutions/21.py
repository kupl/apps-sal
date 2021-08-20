"""
Created on Sat Mar 11 23:20:54 2017

@author: Alexandr
"""
n = int(input())
brackets = input()
max_deep = 0
deep = [0] * n
d = 0
for i in range(n):
    if brackets[i] == '[':
        d += 1
        deep[i] = d
    else:
        deep[i] = d
        d -= 1
max_deep = max(deep)
ans = []
height = max_deep * 2 + 1
for i in range(n):
    x = (max_deep - deep[i]) * 2 + 1
    y = (height - x - 2) // 2
    s = '+' + '|' * x + '+'
    if i != 0 and brackets[i] == ']' and (brackets[i - 1] == '['):
        ans.append(y * ' ' + '-' + x * ' ' + '-' + y * ' ')
        ans.append(' ' * height)
        ans.append(y * ' ' + '-' + x * ' ' + '-' + y * ' ')
    if i != 0 and i != n - 1 and (deep[i] != 1) and (deep[i] > deep[i - 1] or deep[i] > deep[i + 1]):
        s = (y - 1) * ' ' + '-' + s + '-' + (y - 1) * ' '
    else:
        s = y * ' ' + s + y * ' '
    ans.append(s)
for i in zip(*ans):
    print(''.join(i))
