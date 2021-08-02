n = int(input())
a = list(map(int, input().split()))
l = [0] * 9
cnt = 0
for i in a:
    if i < 400:
        l[0] += 1
    elif i < 800:
        l[1] += 1
    elif i < 1200:
        l[2] += 1
    elif i < 1600:
        l[3] += 1
    elif i < 2000:
        l[4] += 1
    elif i < 2400:
        l[5] += 1
    elif i < 2800:
        l[6] += 1
    elif i < 3200:
        l[7] += 1
    else:
        l[8] += 1
for i in range(8):
    if l[i] >= 1:
        cnt += 1

if cnt == 0:
    print(1, l[8])
else:
    print(cnt, cnt + l[8])
