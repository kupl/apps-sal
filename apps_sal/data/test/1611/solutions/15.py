__author__ = 'Utena'
n=int(input())
rods=sorted(list(map(int,input().split())))
total=sum(rods)
t=0
j=0
for i in range(n-1):
    t+=rods[i]
    if t>=total-t:j=1
if j==0:
    print(2*rods[-1]-total+1)
else:
    print(1)
