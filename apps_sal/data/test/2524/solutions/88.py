def readinput():
    n=int(input())
    l=list(map(int,input().split()))
    return n,l

def main(n,a):
    MOD=10**9+7
    hist=[0]*61
    bs=[]
    for i in range(n):
        # s=list(reversed(bin(a[i])[2:]))
        # for j in range(len(s)):
        #     if s[j]=='1':
        #         hist[j]+=1
        # bs.append(s)
        s=bin(a[i])[2:]
        for j in range(len(s)):
            if s[j]=='1':
                hist[len(s)-j-1]+=1

    #print(bs)
    #print(hist)
    sum=0
    # for i in range(n-1):
    #     s=bs[i]
    #     b=1
    #     for j in range(len(s)):
    #         if s[j]=='0':
    #             sum=(sum+hist[j]*b)%MOD
    #         else:
    #             sum=(sum+( n-i-hist[j] )*b)%MOD
    #             hist[j]-=1
    #         b*=2
    #     for j in range(len(s),61):
    #         sum=(sum+hist[j]*b)%MOD
    #         b*=2
    b=1
    for j in range(61):
        sum=(sum+( hist[j]*(n-hist[j])*b )%MOD )%MOD
        b*=2

    return sum

def __starting_point():
    n,l=readinput()
    ans=main(n,l)
    print(ans)

__starting_point()
