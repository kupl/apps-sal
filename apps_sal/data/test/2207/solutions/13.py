rc = input()
rc = rc.split()
r = int(rc[0])
c = int(rc[1])
for i in range(r):
    row = input()
count = 0
for i in range(len(row)):
    if row[i] == 'B' and (i == 0 or row[i - 1] == '.'):
        count += 2
    if row[i] == 'B' and (i == len(row) - 1 or row[i + 1] == '.'):
        count -= 1
print(count)
