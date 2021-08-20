n = int(input())
s = input()
f1 = 0
f2 = 0
res = 0
for i in range(len(s)):
    if s[i] == 'L':
        if f1 == 0:
            f1 = -1
        if f1 == 1:
            res += 1
            f1 = -1
            f2 = 0
    if s[i] == 'R':
        if f1 == 0:
            f1 = 1
        if f1 == -1:
            res += 1
            f1 = 1
            f2 = 0
    if s[i] == 'U':
        if f2 == 0:
            f2 = -1
        if f2 == 1:
            res += 1
            f1 = 0
            f2 = -1
    if s[i] == 'D':
        if f2 == 0:
            f2 = 1
        if f2 == -1:
            res += 1
            f1 = 0
            f2 = 1
if f1 != 0 or f2 != 0:
    res += 1
print(res)
