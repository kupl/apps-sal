n = int(input())
a = list(map(int, input().split()))
d = []
for i in range(1, n-1):
    temp = a[:]
    temp.remove(temp[i])
    tempD = -1
    for x in range(1, len(temp)):
        tempD = max(tempD, temp[x]-temp[x-1])
    d.append(tempD)
d.sort()
print(d[0])

