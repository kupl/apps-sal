n = int(input())
ch = input()
d1 = ch.split()
d2 = []
d = []
for i in d1:
    d2.append(int(i))
j = 0
d2.sort()
for i in d2:
    if i not in d:
        d.append(i)
B = False
while j < len(d) - 2 and B == False:
    if d[j + 2] - d[j] == 2 and d[j + 1] - d[j] == 1 and (d[j + 2] - d[j + 1] == 1):
        B = True
    j += 1
if B:
    print('YES')
else:
    print('NO')
