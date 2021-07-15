N,A,B = list(map(int,input().split()))
ans = 0
for i in range(1,N+1):
  M = i//10000+i%10000//1000+i%1000//100+i%100//10+i%10
  if A <= M and M <= B:
    ans+=i
print(ans)

