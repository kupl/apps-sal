N,X=list(map(int,input().split()))
ryou=[]
for i in range(N):
  ryou.append(int(input()))
amari=X-sum(ryou)
print(N+amari//min(ryou))
