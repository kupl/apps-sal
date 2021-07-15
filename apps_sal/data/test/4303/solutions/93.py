from sys import stdin

def getval():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    return n,k,x

def main(n,k,x):
    idx = k-1
    ans = 0
    if x[0]>=0:
        ans = x[idx]
    elif x[idx]<=0:
        ans = abs(x[0])
    else:
        ans = min(abs(x[0]),abs(x[idx]))*2+max(abs(x[0]),abs(x[idx]))
    for i in range(k,n):
        temp = 0
        #print(ans)
        if x[i-k+1]>=0:
            temp = x[i]
        elif x[i]<=0:
            temp = abs(x[i-k+1])
        else:
            temp = min(abs(x[i]),abs(x[i-k+1]))*2+max(abs(x[i]),abs(x[i-k+1]))
        ans = min(ans,temp)
    print(ans)


def __starting_point():
    n,k,x = getval()
    main(n,k,x)
__starting_point()
