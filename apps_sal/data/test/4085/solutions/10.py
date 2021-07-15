isPrime=[1 for i in range(1000005)]
primes=[]
for i in range(2,1000005):
    if(isPrime[i]==1):
        primes.append(i)
        j=2*i
        while(j<1000005):
            isPrime[j]=0
            j+=i

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return a*b/gcd(a,b)

t=int(input())
while(t>0):
    n=int(input())
    d=list(map(int,input().split()))
    d.sort()
    ans=1
    flag=1
    for i in range(len(d)-1):
        if(d[i]*d[n-i-1]!=d[i+1]*d[n-i-2]):
            flag=0
            break
    if(flag==0):
        print(-1)
    else:
        ans=d[0]*d[-1]
        amt=1
        x=ans
        for i in primes:
            if(ans%i==0):
                cnt=1
                while(x%i==0):
                    cnt+=1
                    x/=i
                amt*=cnt
        if(x>1):
            amt*=2
        if(amt-2==len(d)):
            print(int(ans))
        else:
            print(-1)
    """    
    for i in d:
        ans=lcm(ans,i)
        if(ans>10**30):
            print(-1)
            break
    if(ans>10**30):
        t-=1
        continue 
    if(ans==d[-1]):
        po=1
        flag=1
        for i in d:
            po*=d[0]
            if(po!=i):
                flag=0
        if(flag==1):
            print(int(ans*d[0]))
        else:
            print(-1)
    else:
        amt=1
        x=ans
        for i in primes:
            if(ans%i==0):
                cnt=1
                while(x%i==0):
                    cnt+=1
                    x/=i
                amt*=cnt
        if(x>1):
            amt*=2
        if(amt-2==len(d)):
            print(int(ans))
        else:
            print(-1)
    """
    t-=1

