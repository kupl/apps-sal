__author__ = 'yarsanich'
import math
n = int(input())
"""
Flag = False
k = 0
check = (0**n) % n
ans = 1
while Flag == False:
      k += 1
      #print((k**n)%n)
      if ((k**n)%n == check):
          print(ans)
          break
      else:
          ans += 1
"""
ans = 1
if (n%2 == 0):
    ans *= 2
    while n%2 == 0:
        n /= 2
i = 3
while i<=int(math.sqrt(n))+1:
    if (n % i == 0):
        ans *= i
        while (n % i == 0):
            n /= i
    i += 2
if (n > 2):
    ans *= n
print(int(ans))
