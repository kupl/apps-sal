mod=10**9+7
num,k=map(int,input().rstrip().split())
mai=list(map(int, input().rstrip().split()))
main=sorted(mai,key=abs,reverse=True)
result=1
def findplus_plus(x):
    for i in range(x,len(main)):
        if main[i]>=0:
            return main[i]
    return ''
def findplus_minus(x):
    for i in range(x,len(main)):
        if main[i]<0:
            return main[i]
    return ''
def findminus_plus(x):
    for i in range(x-1,-1,-1):
        if main[i]>=0:
            return main[i]
    return ''
def findminus_minus(x):
    for i in range(x-1,-1,-1):
        if main[i]<0:
            return main[i]
    return ''

if num==k:
    for i in main:
        result*=i
        result%=mod
elif sorted(main)[len(sorted(main))-1]<0:
    if (k%2)==0:
        for i in range(k):
            result*=main[i]
            result%=mod
    else:
        for i in range(len(main)-1,len(main)-1-k,-1):
            result*=main[i]
            result%=mod

else:
    count=0
    for i in range(k):
        if main[i]<0:
            count+=1
        result*=main[i]
        result%=mod
    if (count%2)==1:
        minplus=findminus_plus(k)
        minminus=findminus_minus(k)
        maxplus=findplus_plus(k)
        maxminus=findplus_minus(k)
        if type(maxplus)==type(''):
            plusplus=-1
            minusminus=minminus*maxminus
        else:
            if type(maxminus)==type('') or type(minplus)==type(''):
                minusminus=-1
                plusplus=0
            else:
                minusminus=minminus*maxminus
                plusplus=minplus*maxplus
        if plusplus>minusminus:
            main.remove(minminus)
            result=1
            for i in range(k-1):
                result*=main[i]
                result%=mod
            result*=maxplus
        elif plusplus<=minusminus:
            main.remove(minplus)
            result=1
            for i in range(k-1):
                result*=main[i]
                result%=mod
            result*=maxminus
            
print(result%mod)
