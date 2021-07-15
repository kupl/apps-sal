n,l,v,o,k=list(map(int,input().split()))
T=(n+k-1)//k
e=1-v/o
L=l/v/(T/o+T*e/(v+o)-e/(v+o)-1/o+1/v)
print((l-L)/v+L/o)

