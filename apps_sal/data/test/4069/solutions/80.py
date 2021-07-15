#abc175c
x,k,d=list(map(int,input().split()))
x=abs(x)
t=x//d
if k<t:
 print((x-k*d))
else:
 print((abs(x%d-(k-t)%2*d)))

