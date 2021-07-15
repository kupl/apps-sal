a,b=map(int,input().split())
n = input()
m = [0]*a
for i in range(1,a):
  if n[i-1:i+1]=="AC":
    m[i]=m[i-1]+1
  else:
    m[i]=m[i-1]
for j in range(b):
  s,t=map(int,input().split())
  print(m[t-1]-m[s-1])
