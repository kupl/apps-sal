n, k = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
coun = 1
d = 0
i = 1
while i < n:
    d += p[i] - p[i - 1]
    if k < p[i] - p[i - 1]:
        coun = -1
        break
    if k < d:
        coun += 1
        d = 0
        continue
    i += 1
print(coun)
