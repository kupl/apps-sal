N = int(input())
X = list(map(int, input().split()))
small = 10000000
temp = 0
p_max = max(X)

for p in range(1, p_max + 1):
  for i in range(N):
    temp += (X[i] - p)**2
    
  if temp < small:
    small = temp
  
  temp = 0
  
print(small)

