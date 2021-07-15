N=int(input())
C=list(input())
rednum=C.count('R')
rednumleft=0
for i in range(rednum):
    if C[i]=='R':
        rednumleft+=1
print(rednum-rednumleft)
