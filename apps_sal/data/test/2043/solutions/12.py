__author__ = 'ruckus'

s = input()
t = input()
inlines = []
j = 0
for i in range(len(t)):
    if t[i] == s[j]:
        if j == 0:
            inlines.append([i])
        j += 1
        if j >= len(s):
            inlines[len(inlines)-1].append(i)
            break
j = len(s)-1
for i in range(len(t)-1, -1, -1):
    if t[i] == s[j]:
        if j == len(s)-1:
            inlines.append([i])
        j -= 1
        if j < 0:
            inlines[1].append(i)
            break
if len(inlines) < 2 or len(inlines[1]) < 2 or inlines[1][1]-inlines[0][1] < 0:
    print(0)
else:
    print(inlines[1][1]-inlines[0][1])
