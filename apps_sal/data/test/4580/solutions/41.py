N = int(input())
a = list(map(int, input().split()))
color = [0] * 9
for i in range(N):
    if 1 <= a[i] <= 399:
        color[0] += 1
    elif 400 <= a[i] <= 799:
        color[1] += 1
    elif 800 <= a[i] <= 1199:
        color[2] += 1
    elif 1200 <= a[i] <= 1599:
        color[3] += 1
    elif 1600 <= a[i] <= 1999:
        color[4] += 1
    elif 2000 <= a[i] <= 2399:
        color[5] += 1
    elif 2400 <= a[i] <= 2799:
        color[6] += 1
    elif 2800 <= a[i] <= 3199:
        color[7] += 1
    elif 3200 <= a[i]:
        color[8] += 1
count = 0
for i in range(8):
    if color[i] != 0:
        count += 1
if count == 0:
    print(1, count + color[8])
else:
    print(count, count + color[8])
