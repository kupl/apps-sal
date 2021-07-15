n=int(input())
t,a=map(int,input().split())
h=list(map(int,input().split()))

p=[]

for i in range(n):
  q=(t-0.006*h[i])
  p.append(abs(q-a))

print(p.index(min(p))+1)
