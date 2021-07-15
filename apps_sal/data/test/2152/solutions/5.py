n=int(input())
p=[list(map(int,input().split())) for i in range(n)]
m=1000
s=0
for x in p:
   if m>x[1]: m=x[1]
   s+=x[0]*m
print(s)
