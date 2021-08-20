x = int(input())
sop = [int(i) for i in input().split()]
tem = [int(j) for j in input().split()]
for i in range(x):
    sm = 0
    for j in range(i + 1):
        if sop[j] >= tem[i]:
            sm += tem[i]
            sop[j] -= tem[i]
        else:
            sm += sop[j]
            sop[j] = 0
    print(sm, end=' ')
