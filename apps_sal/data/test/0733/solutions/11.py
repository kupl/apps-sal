# for finding lcm we need to know gcd
def gcd(a,b):
    while b!=0:
        temp=b
        b=a%b
        a=temp
    return a
def lcm(a,b):
    g=gcd(a,b)
    lc=(a*b)//g
    return lc

while(1):
    try:
        a=list(map(int,input().split()))
        maxi=a[0] if a[0]>a[1] else a[1]
        if maxi==a[0]:
            mini=a[1]
         
        else:
            maxi=a[1]
            mini=a[0]
        l=lcm(maxi,mini)
        c=0
        maxi=a[2] if a[2]>a[3] else a[3]
        if maxi==a[2]:
            mini=a[3]
        else:
            maxi=a[3]
            mini=a[2]
        print(maxi//l-(mini-1)//l)
        
    except EOFError:
        break

            
            
        
        
        
        

