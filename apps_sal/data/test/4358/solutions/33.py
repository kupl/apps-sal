N = int(input())
data = list(range(N))
m = 0
while m < N:
    data[m] = int(input())
    m += 1

kei = 0
max = 0
for i in range(len(data)):
    kei += data[i]
    if max < data[i]:
        max = data[i]

kei = kei - max / 2
print((int(kei)))

