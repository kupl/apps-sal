from math import*
n = int(input())
som = 0
ch = []
ch2 = []
for i in range(n):
    f = float(input())
    ch.append(floor(f))
    ch2.append(f)
    som += floor(f)
i = 0
while som != 0:
    if ceil(ch2[i]) != ch2[i]:
        som += 1
        ch[i] += 1
    i += 1
for i in range(n):
    print(ch[i])
