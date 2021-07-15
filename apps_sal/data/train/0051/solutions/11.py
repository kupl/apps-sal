from sys import *

t=int(stdin.readline())
for i in range(t):
    n,k,d1,d2=(int(z) for z in stdin.readline().split())
    vars=[[2*d1+d2,2*d2+d1],[2*d2+d1,2*d1+d2],[2*max(d1,d2)-min(d1,d2),d1+d2], [d1+d2,2*max(d1,d2)-min(d1,d2)]]
    y=False
    for i in vars:
        if i[0]<=k and i[0]%3==k%3 and n-k-i[1]>=0 and (n-i[1]-k)%3==0:
            print("yes")
            y=True
            break
    if not y:
        print("no")
