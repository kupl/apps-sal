t=int(input())
for you in range(t):
    l=input().split()
    p=int(l[0])
    f=int(l[1])
    l=input().split()
    cnts=int(l[0])
    cntw=int(l[1])
    l=input().split()
    s=int(l[0])
    w=int(l[1])
    maxa=[]
    if(s>w):
        w,s=s,w
        cnts,cntw=cntw,cnts
    for i in range(cnts+1):
        remp=p-i*s
        if(remp<0):
            break
        z=i+min(remp//(w),cntw)
        remsw=cnts-(i)
        remax=(cntw-min(remp//(w),cntw))
        my=f
        z+=min(my//s,remsw)
        my-=s*min(my//s,remsw)
        z+=min(my//w,remax)
        maxa.append(z)
    print(max(maxa))

