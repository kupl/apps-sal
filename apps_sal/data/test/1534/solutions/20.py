"""
Created on Wed Oct 25 09:07:32 2017

@author: savit
"""
s = input()
startpos = 0
max1 = 0
temp = 0
beststart = []
for i in range(len(s)):
    if s[i] == 'a':
        temp += 1
        if temp > max1:
            max1 = temp
            startpos = i + 1
    else:
        temp -= 1
    beststart.append((max1, startpos))
beststart.append((0, -1))
max2 = 0
temp = 0
endpos = len(s)
for i in range(len(s) - 1, -1, -1):
    if s[i] == 'a':
        temp += 1 + (beststart[i - 1][0] - beststart[i][0])
        if max2 < temp:
            max2 = temp
            endpos = i
    else:
        temp -= 1
ans = 0
if endpos != len(s):
    startpos = beststart[endpos][1]
if startpos == -1:
    startpos = 0
for i in range(startpos):
    if s[i] == 'b':
        ans += 1
for i in range(startpos, endpos):
    if s[i] == 'a':
        ans += 1
for i in range(endpos, len(s)):
    if s[i] == 'b':
        ans += 1
print(len(s) - ans)
