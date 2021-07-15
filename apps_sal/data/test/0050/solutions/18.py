n,m,r=(int(i) for i in input().split())
s=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
m=min(s)
a=r//m
k=r-m*(r//m)
p=a*max(b)
print(max(p+k,r))

