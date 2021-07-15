N,M = map(int,input().split())
array = list(map(int,input().split()))
ans = [1]*N
for i in range (M):
  A,B = map(int,input().split())
  if array[A - 1] < array[B - 1]:
    ans[A - 1] = 0
  elif array[A - 1] > array[B - 1]:
    ans[B - 1] = 0
  else:
    ans[A-1],ans[B-1] = 0,0
print( sum(ans) )
