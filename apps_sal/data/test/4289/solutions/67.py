n=int(input())
t,a=map(int,input().split())
m=10000
h=list(map(int,input().split()))
for i in range(n):
  x=t-h[i]*0.006
  m=min(m,abs(x-a))

for i in range(n):
  if m==abs((t-h[i]*0.006)-a):
    print(1+i)
