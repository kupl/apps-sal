import sys

n = int(sys.stdin.readline())
data = sys.stdin.readline().split(" ")
a = [int(x) for x in data]

if (n == 1):
    print(1)
    return

pos = [0 for i in range(n + 1)]
for i in range(n):
    pos[a[i]] = i

record = [0 for i in range(n)]
gainWhenRemoved = [0 for i in range(n)]

max1 = -1
max2 = -1

for i in range(n):
    if (a[i] > max1):
        record[i] = 1
    else:
        if (max2 == -1 or max2 < a[i]):
            max1pos = pos[max1]
            gainWhenRemoved [max1pos] = gainWhenRemoved [max1pos] + 1

    if (a[i] > max1):
        max2 = max1
        max1 = a[i]
    else:
        if (a[i] > max2):
            max2 = a[i]

numRecord = sum(record)

sol = -1
index = 0;
for i in range(n):
    tmp = numRecord - record [i] + gainWhenRemoved [i]
    if (sol < tmp) or (sol == tmp and a[index] > a[i]):
        sol = tmp
        index = i

print(a[index])
