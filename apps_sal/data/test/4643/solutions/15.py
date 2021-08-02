import time
kal = list(map(int, input().split()))
p = kal[1:]
kaleee = []
for i in range(6300):
    kaleee.append(i)
    kaleee.count(i)
p.sort()
for i in p:
    print(i, end=' ')
