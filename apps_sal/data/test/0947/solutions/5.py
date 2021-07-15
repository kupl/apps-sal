t=int(input())
for you in range(t):
    n=int(input())
    if(n%2==0):
        print(n//2,n//2)
    else:
        l=[1]
        i=2
        while(i*i<=n):
            if(n%i==0):
                l.append(i)
                if(i!=n//i):
                    l.append(n//i)
            i+=1
        z=max(l)
        print(n-z,z)

