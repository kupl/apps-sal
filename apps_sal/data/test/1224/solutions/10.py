import math

n = int(input())

for i in range(1,26):
  for j in range(1,38):
    if 3**j + 5**i == n:
      print(j,i)
      return
    
print(-1)
