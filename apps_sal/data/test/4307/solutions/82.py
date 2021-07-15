from math import *

N = int(input())

def count(n):
   rt = sqrt(n)
   result = 0
   if int(rt) ** 2 == n:
      for i in range(1, int(rt) + 1):
         if n % i == 0:
            result += 1
      result = (2 * result) - 1
   else:
      for i in range(1, int(rt) + 1):
         if n % i == 0:
            result += 1
      result *= 2
   return result

ans = 0

for i in range(1, N + 1):
   if (i % 2 == 1) and (count(i) == 8):
      ans += 1

print(ans)
