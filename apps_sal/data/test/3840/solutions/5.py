t = int(input())
line = input()
lis = line.split()
lis = [int(i) for i in lis]
if t == 1 or t % 2 == 0:
    print('-1')
    quit()
count = 0
i = t
while i >= 4:
    if i % 2 == 1:
        p = i - 1
        q = int(p / 2)
        count = count + lis[i - 1]
        lis[p - 1] = lis[p - 1] - lis[i - 1]
        if lis[p - 1] < 0:
            lis[p - 1] = 0
        lis[q - 1] = lis[q - 1] - lis[i - 1]
        if lis[q - 1] < 0:
            lis[q - 1] = 0
        lis[i - 1] = 0
    else:
        p = i + 1
        q = int(i / 2)
        count = count + lis[i - 1]
        lis[p - 1] = lis[p - 1] - lis[i - 1]
        if lis[p - 1] < 0:
            lis[p - 1] = 0
        lis[q - 1] = lis[q - 1] - lis[i - 1]
        if lis[q - 1] < 0:
            lis[q - 1] = 0
        lis[i - 1] = 0
    i = i - 1
m = max(lis[0], lis[1], lis[2])
count = count + m
print(count)
