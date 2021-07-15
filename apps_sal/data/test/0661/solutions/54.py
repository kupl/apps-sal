m,k=map(int,input().split())
x=[*range(1<<m)]
print(*x+x[::-1]if k<1else[k]+x[k+1:]+x[:k]+[k]+x[k-1::-1]+x[:k:-1]if(k<2**m)&(m>1)else[-1])
