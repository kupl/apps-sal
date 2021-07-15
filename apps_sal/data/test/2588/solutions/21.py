t=int(input())
for i in range(t):
    n,a,b=[int(x) for x in input().split()]
    s=[int(x) for x in list(input())]
    gas=n
    h=n+1
    index=-1
    one=-1
    for i in range(n):
        if s[i]==0:
            if index!=-1:
                h+=i-index+1
                gas+=2
                index=-1
                one=i-1
        else:
            if index==-1:
                index=i
                if one!=-1 and 2*a>(i-one-2)*b:
                    gas-=2
                    h+=i-one-2
    print(gas*a+h*b)

                
    
        

