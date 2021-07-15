N,K=list(map(int,input().split()))
A=[int(x) for x in input().split()]
already=set()
already.add(1)
placelist=[1]
numofmove=0
now=1
loopstart=0
loopend=0
remain=0
while(numofmove<K):
    now=A[now-1]
    #print(now)
    numofmove+=1
    placelist.append(now)
    if now in already:
        loopstart=placelist.index(now)
        loopend=numofmove
        #print(remain,numofmove,loopstart,loopend,placelist)
        remain=(K-numofmove)%(loopend-loopstart)
        for i in range(remain):
            now=A[now-1]
        break 
    else:
        already.add(now)
print(now)

