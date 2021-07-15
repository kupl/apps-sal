from itertools import combinations
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = [a[i]%m for i in range(n)]
if len(set(b)) < n:
  print(0)
  return
ans = 1
for i,j in combinations(a,2):
  ans = (ans*abs(i-j))%m
print(ans)
