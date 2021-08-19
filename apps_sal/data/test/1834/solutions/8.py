n = int(input())
ch = input()
d = ch.split()
for i in range(n):
    d[i] = int(d[i])
d.sort()
d1 = []
i = 0
j = 0
while j < n:
    d1.append(d[i])
    j += 1
    if j < n:
        j += 1
        d1.append(d[n - i - 1])
    i += 1
B = False
for i in range(n):
    if d1[i] < d1[i - 1] and (i + 1) % 2 == 0:
        B = True
    if d1[i] > d1[i - 1] and (i + 1) % 2 != 0:
        B = True
if B == False:
    for i in d1:
        print(i, end=' ')
else:
    print('Impossible')
