import sys
input=sys.stdin.readline
t=int(input())
for you in range(t):
    n=int(input())
    l=input().split()
    li=[int(i) for i in l]
    hashi=dict()
    count=0
    for i in li:
        for j in range(31,-1,-1):
            if(i&(1<<j)):
                ans=j
                break
        if(ans in hashi):
            count+=hashi[ans]
            hashi[ans]+=1
        else:
            hashi[ans]=1
    print(count)

