def intersect(l1,r1,l2,r2):
    if(l1>r2 and r1>r2):
        return 0
    if(r1<l2 and r1<r2):
        return 0
    return 1
t=int(input())
for you in range(t):
    l=input().split()
    n=int(l[0])
    x=int(l[1])
    m=int(l[2])
    ans=0
    done=0
    currleft=-1
    currright=-1
    for i in range(m):
        l=input().split()
        left=int(l[0])
        right=int(l[1])
        if(done==0):
            if(left<=x and x<=right):
                done=1
                currleft=left
                currright=right
        else:
            if(intersect(left,right,currleft,currright)):
                currleft=min(left,currleft)
                currright=max(right,currright)
    print(currright-currleft+1)        

