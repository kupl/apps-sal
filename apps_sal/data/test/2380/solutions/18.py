import sys
from bisect import bisect_left,bisect,bisect_right

icase=0
if icase==0:
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    d=[]
    cb=[[0]*2 for i in range(m)]
    for i in range(m):
        bi,ci=list(map(int,input().split()))
        cb[i]=[ci,bi]
elif icase==1:
    n,m=3,2
    a=[1, 4, 5]
    cb=[[5, 1], [3, 2]]
elif icase==3:
    n,m=3,2
    a=[100, 100, 100]
    cb=[[99, 3], [99, 3]]
elif icase==2:
    n,m=10,3
    a=[1, 4, 5, 5, 7, 8, 13, 33, 52, 100]
    cb=[[30, 4], [10, 3], [4, 1]]
elif icase==4:
    n,m=11,3
    a=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    cb=[[1000000000, 4], [1000000000, 3], [1000000000, 3]]
elif icase==5:
    f=open(r"C:\Users\nishi\999atcoder\ABCD040-151\ABC127D\testcase_13_in.dat")
    ll=f.readline()
    n,m=list(map(int,ll.split()))
    ll=f.readline()
    a=list(map(int,ll.split()))
    d=[]
    cb=[[0]*2 for i in range(m)]
    for i in range(m):
        ll=f.readline()
        bi,ci=list(map(int,ll.split()))
        cb[i]=[ci,bi]
    f.close()
    ans=99913215738299
elif icase==6:
    f=open(r"C:\Users\nishi\999atcoder\ABCD040-151\ABC127D\testcase_12_in.dat")
    ll=f.readline()
    n,m=list(map(int,ll.split()))
    ll=f.readline()
    a=list(map(int,ll.split()))
    d=[]
    cb=[[0]*2 for i in range(m)]
    for i in range(m):
        ll=f.readline()
        bi,ci=list(map(int,ll.split()))
        cb[i]=[ci,bi]
    f.close()
    ans=95821339675952

a.sort()
cb.sort(reverse=True)

if cb[0][0]<=a[0]:
    print((sum(a)))
    return
    
asum=0
isum=0
isumm=0
for i in range(m):
    isum+=cb[i][1]
    if isum>n:
        if a[-1]<=cb[i][0]:
#        print("A",i)
            asum+=cb[i][0]*(n-isumm)
            print(asum)
            return
#    isum=min(isum,n)
#    print(i,isum,a[isum-1])
        else:
#        print("C",i)
            ii=bisect_right(a,cb[i][0])
            asum+=cb[i][0]*(ii-isumm)
#        print(ii,isumm,asum)
#        asum+=sum(a[ii:isum])
            asum+=sum(a[ii:])
            print(asum)
            return
    if a[isum-1]<=cb[i][0]:
        asum+=cb[i][0]*cb[i][1]
#        asum+=cb[i][0]*(isum-isumm)
#        print("B",i,isum,asum)
        isumm=isum
        continue
    else:
#        print("C",i)
        ii=bisect_right(a,cb[i][0])
        asum+=cb[i][0]*(ii-isumm)
#        print(ii,isumm,asum)
#        asum+=sum(a[ii:isum])
        asum+=sum(a[ii:])
        print(asum)
        return
#        isumm=isum
#        break
    isumm=isum
    
#if isumm<n:
asum+=sum(a[isumm:])
        
print(asum)

