n = int(input())
min_A = 10**9+7
max_A = -1
for i in input().split():
  tmp = int(i)
  max_A = max(tmp,max_A)
  min_A = min(min_A,tmp)
  
print((abs(max_A-min_A)))

