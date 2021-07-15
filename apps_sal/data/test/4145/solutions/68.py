import math

def prime(n):
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

n = int(input())
while True:
  if prime(n):
    break
  else:
    n += 1
print(n)
