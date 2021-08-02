from sys import stdin
line = stdin.readline().rstrip()


count0 = 0
count1 = 0
index = 0
found2 = False
for c in line:
    index += 1
    if c == '0':
        count0 += 1
    if c == '2':
        found2 = True
        break
while count0 > 0:
    count0 -= 1
    print('0', end='')
for c in line:
    if c == '1':
        print('1', end='')
if found2:
    print('2', end='')
for i in range(index, len(line)):
    if line[i] != '1':
        print(line[i], end='')
