from collections import defaultdict
n = int(input())
s = input()
t = input()
col1 = defaultdict(list)
col2 = defaultdict(list)
any1 = []
any2 = []
a = ord('a')
for i in range(n):
    if s[i] == '?':
        any1.append(i)
    else:
        col1[ord(s[i]) - a].append(i)
for i in range(n):
    if t[i] == '?':
        any2.append(i)
    else:
        col2[ord(t[i]) - a].append(i)
rec = []
mo1 = []
mo2 = []
for i in range(26):
    for j in range(max(len(col1[i]), len(col2[i]))):
        if j < min(len(col1[i]), len(col2[i])):
            rec.append((col1[i][j], col2[i][j]))
        elif len(col1[i]) > len(col2[i]):
            mo1.append(col1[i][j])
        else:
            mo2.append(col2[i][j])
while len(mo1) > 0 and len(any2) > 0:
    (a, b) = (mo1.pop(), any2.pop())
    rec.append((a, b))
while len(mo2) > 0 and len(any1) > 0:
    (a, b) = (any1.pop(), mo2.pop())
    rec.append((a, b))
for i in range(min(len(any1), len(any2))):
    rec.append((any1[i], any2[i]))
print(len(rec))
for (i, j) in rec:
    print(i + 1, j + 1)
