from math import gcd
def count(x,a,n):
        c=0
        t=x
        while(1):
                x=a[x-1]
                c+=1
                if t==x:
                        #print(t,x)
                        break
                if c>=n:
                        return 0
                        break
        if c%2==0:
                return c//2
        else:
                return c
def xyz():
        n=int(input())
        a=[int(i) for i in input().split()]
        l=1
        for i in range(n):
                p=count(i+1,a,n)
                if p==0:
                        return -1
                l=(p*l)//(gcd(p,l))
        return l
print(xyz())
        
        
        

