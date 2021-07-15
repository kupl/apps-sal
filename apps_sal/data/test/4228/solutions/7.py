N,L = map(int,input().split())

apples = [i+L-1 for i in range(1,N+1)]

ans = float("inf")
res = float("inf")

for apple in apples:
  if ans > abs(apple):
    ans = min(ans,abs(apple))
    res = apple
  
print(sum(apples) - res)
