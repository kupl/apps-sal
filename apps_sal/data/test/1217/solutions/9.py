n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [[int(i), 0] for i in input().split()]
for i in range(m):
    b[i][1] = i
a.sort()
b.sort(key=lambda x: x[0])
ress = [0] * m
i = j = 0
res = 0
while i < len(a) and j < len(b):
    if a[i] <= b[j][0]:
        res += 1
        i += 1
    else:
        ress[b[j][1]] = res
        j += 1
while j < len(b):
    ress[b[j][1]] = res
    j += 1
for i in ress:
    print(i, end=" ")
