from fractions import gcd
n=int(input())
count=0
ip=list(map(int,input().split()))
op=[ip[0]]
if n==1:
    print(0)
    print(ip[0])
else:
    for i in range(n-1):
        if gcd(ip[i],ip[i+1])!=1:
            for j in range(2,100000000):
                if gcd(ip[i],j)==1 and gcd(ip[i+1],j)==1:
                    op.append(j)
                    op.append(ip[i+1])                
                    count+=1
                    break
        else:
            op.append(ip[i+1])
    print(count)
    for i in op:
        print(i,end=' ')

