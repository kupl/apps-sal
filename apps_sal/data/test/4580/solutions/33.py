n = int(input())
a = sorted(map(int, input().split()))

c = [0] * 9
for num in a:
    if num < 400:
        c[0] += 1
    elif num < 800:
        c[1] += 1
    elif num < 1200:
        c[2] += 1
    elif num < 1600:
        c[3] += 1
    elif num < 2000:
        c[4] += 1
    elif num < 2400:
        c[5] += 1
    elif num < 2800:
        c[6] += 1
    elif num < 3200:
        c[7] += 1
    else:
        c[8] += 1
mi = 0
ma = 0
for i in range(8):
    if c[i] >= 1:
        mi += 1
        ma += 1
ma += c[8]
if mi == 0:
    if c[8] >= 1:
        mi += 1
print((str(mi) + " " + str(ma)))
