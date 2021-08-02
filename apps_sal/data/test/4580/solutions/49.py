n = int(input())
a = list(map(int, input().split()))
data = [0] * 9
for i in a:
    if 1 <= i <= 399:
        data[0] += 1
    elif 400 <= i <= 799:
        data[1] += 1
    elif 800 <= i <= 1199:
        data[2] += 1
    elif 1200 <= i <= 1599:
        data[3] += 1
    elif 1600 <= i <= 1999:
        data[4] += 1
    elif 2000 <= i <= 2399:
        data[5] += 1
    elif 2400 <= i <= 2799:
        data[6] += 1
    elif 2800 <= i <= 3199:
        data[7] += 1
    elif 3200 <= i:
        data[8] += 1
min = 0
for i in range(8):
    if data[i] != 0:
        min += 1
if min != 0:
    print(min, min + data[8])
else:
    print(1, data[8])
