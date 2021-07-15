import math
x = int(input())

while True:
  a = int(math.sqrt(x))
  for y in range(2,a+1):
    if x % y == 0:
      break
  else:
    ans = x
    break
  x += 1

  
print(ans)

