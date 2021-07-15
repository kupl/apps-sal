import math
def isprime(n):
  if n == 2:
    return True
  elif n % 2 == 0:
    return False
  else:
    for i in range(3,math.ceil(math.sqrt(n))+1,2):
      if n % i == 0:
        return False
    return True

x = int(input())
ans = 0
if x == 2:
  ans = 2
else:
  if x % 2 == 0:
    st = x+1
  else:
    st = x
  for i in range(st,100001):
    if isprime(i) == True:
      ans = i
      break
  if ans == 0:
    ans = 100003
print(ans)
