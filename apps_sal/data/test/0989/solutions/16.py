import sys
n, k = list(map(int, input().split()))
num = [int(x) for x in input().split()]
num.sort()
if (n == 1):
    print(0)
    return
pre = 0
pree = num[0]
lat = n - 1
latt = num[n - 1]
pren = 1
latn = 1

while (k > 0):
    while (num[pre + 1] == pree and pre + 1 < lat):
        pre += 1
        pren += 1
    while (num[lat - 1] == latt and pre < lat - 1):
        lat -= 1
        latn += 1
    if (pren > k and latn > k):
        break;
    if (pree < latt):
        if (pren < latn):
            if (pren * (num[pre + 1] - num[pre]) <= k):
                k -= pren * (num[pre + 1] - num[pre])
                pre += 1
                pren += 1
                pree = num[pre]
            else:
                pree += k // pren
                k %= pren
        else:
            if (latn * (num[lat] - num[lat - 1]) <= k):
                k -= latn * (num[lat] - num[lat - 1])
                lat -= 1
                latn += 1
                latt = num[lat]
            else:
                latt -= k // latn
                k %= latn
    else:
        break;

print(latt - pree)
