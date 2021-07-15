b=input().split()
core=[]
kcore=int(b[0])
ktact=int(b[1])
for i in range(kcore):
    work=input().split()
    core.append([])
    for j in range(ktact):
        core[i].append(int(work[j]))
#...
zmemory=[]
for i in range(int(b[2])):
    zmemory.append(0)
zcore=[]
answer=[]
for i in range(kcore):
    zcore.append(0)
    answer.append(0)
#...
for i in range(ktact):
    freecore=[]
    for j in range(kcore):
        if zcore[j]==0:
            freecore.append(j)
    for j in freecore:
        if not(core[j][i]==0):
            if zmemory[core[j][i]-1]:
                zcore[j]=1
                answer[j]=i+1
            for k in freecore:
                if not(k==j):
                    if core[j][i]==core[k][i]:
                        zmemory[core[j][i]-1]=1
                        zcore[j]=1
                        answer[j]=i+1
                        zcore[k]=1
                        answer[k]=i+1
#...
for i in range(kcore):
    print(answer[i])

