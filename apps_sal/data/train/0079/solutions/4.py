import sys
input=sys.stdin.readline
t=int(input())
for you in range(t):
    n=int(input())
    z=n
    primes=[]
    i=2
    while(i*i<=z):
        if(z%i==0):
            primes.append(i)
            while(z%i==0):
                z=z//i
        i+=1
    if(z!=1):
        primes.append(z)
    hashi=dict()
    for i in primes:
        hashi[i]=[]
    hashinew=dict()
    new=[]
    k=len(primes)
    hasho=dict()
    if(k>2):
        for i in range(k):
            new.append(primes[i]*primes[(i+1)%k])
            hasho[primes[i]*primes[(i+1)%k]]=1
    if(k==2):
        hasho[primes[0]*primes[1]]=1
    i=2
    while(i*i<=n):
        if(n%i==0):
            num1=i
            num2=n//i
            if(num1 not in hasho):
                for j in primes:
                    if(num1%j==0):
                        break
                hashi[j].append(num1)
            if(num2!=num1 and num2 not in hasho):
                for j in primes:
                    if(num2%j==0):
                        break
                hashi[j].append(num2)
        i+=1
    for j in primes:
        if(n%j==0):
            break
    hashi[j].append(n)
    done=dict()
    if(len(primes)==1):
        for i in hashi[primes[0]]:
            print(i,end=" ")
        print()
        print(0)
        continue
    if(len(primes)==2):
        if(primes[0]*primes[1]==n):
            print(primes[0],primes[1],n)
            print(1)
        else:
            for i in hashi[primes[0]]:
                print(i,end=" ")
            for i in hashi[primes[1]]:
                print(i,end=" ")
            print(primes[0]*primes[1],end=" ")
            print()
            print(0)
        continue
    for i in range(k):
        for j in hashi[primes[i]]:
            print(j,end=" ")
        ko=primes[i]*primes[(i+1)%k]
        print(ko,end=" ")
    print()
    print(0)

