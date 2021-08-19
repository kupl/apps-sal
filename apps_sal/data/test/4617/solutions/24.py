data1 = input()
data2 = input()
count = 3 - 1
sw = 0
i = 0
j = len(data2) - 1
while i <= count:
    if data1[i] == data2[j]:
        sw += 1
    i += 1
    j -= 1
if sw == 3:
    print('YES')
else:
    print('NO')
