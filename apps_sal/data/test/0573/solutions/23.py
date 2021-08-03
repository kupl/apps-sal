n = int(input())
a = [int(i) for i in input().split()]
d = dict()
d[1] = 0
d[2] = 0
for i in range(n):
    if a[i] == 1:
        d[1] += 1
    else:
        d[2] += 1

if d[1] >= d[2]:
    print(d[2] + (d[1] - d[2]) // 3)
else:
    print(d[1])
