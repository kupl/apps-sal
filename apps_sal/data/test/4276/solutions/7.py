N,T=map(int,input().split())
cost=1000000
num=-1
for i in range(N):
  c,t=map(int,input().split())
  if t<=T and cost > c:
    cost = c
    num = i+1
print(cost if num > 0 else 'TLE')
