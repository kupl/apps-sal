N = int(input())
array = list(map(int,input().split()))
ans = [0]*N
for i in array:
  ans[i-1] += 1

for i in range(N):
  print( ans[i] )
