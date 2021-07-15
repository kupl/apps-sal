n = int(input())
tab = [int(x) for x in input().split(' ')]
stab = tab.copy()
stab.sort()
sumtab = [0,tab[0]]
sumstab = [0,stab[0]]
for x in range(2,len(tab)+1):
    sumtab.append(sumtab[x-1]+tab[x-1])
for x in range(2,len(stab)+1):
    sumstab.append(sumstab[x-1]+stab[x-1])
m = int(input())
for i in range(m):
    query = [int(x) for x in input().split(' ')]
    if query[0]==1:
        print(sumtab[query[2]] - sumtab[query[1]-1])
    else:
        print(sumstab[query[2]] - sumstab[query[1]-1])

