s,x=list(map(int,input().split()))
print(0 if (s<x or (s-x)%2 or ((s-x)//2)&(x)!=0) else 2**(list(bin(x)).count('1'))-2*(s==x) )

