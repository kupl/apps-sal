N = int(input())
a = [int(v) for v in input().split(' ')]
l = [0] * 9
for i in range(N):
    rate = a[i]
    if rate < 400:
        l[0] += 1
    elif rate < 800:
        l[1] += 1
    elif rate < 1200:
        l[2] += 1
    elif rate < 1600:
        l[3] += 1
    elif rate < 2000:
        l[4] += 1
    elif rate < 2400:
        l[5] += 1
    elif rate < 2800:
        l[6] += 1
    elif rate < 3200:
        l[7] += 1
    else:
        l[8] += 1
uniq_n = 0
for i in range(8):
    if l[i] != 0:
        uniq_n += 1
min_v = 1 if uniq_n == 0 else uniq_n
max_v = uniq_n + l[8]
print(min_v, max_v)
