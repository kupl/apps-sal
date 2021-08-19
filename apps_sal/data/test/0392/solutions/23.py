__author__ = 'yarsanich'
import math
n = int(input())
'\nFlag = False\nk = 0\ncheck = (0**n) % n\nans = 1\nwhile Flag == False:\n      k += 1\n      #print((k**n)%n)\n      if ((k**n)%n == check):\n          print(ans)\n          break\n      else:\n          ans += 1\n'
ans = 1
if n % 2 == 0:
    ans *= 2
    while n % 2 == 0:
        n /= 2
i = 3
while i <= int(math.sqrt(n)) + 1:
    if n % i == 0:
        ans *= i
        while n % i == 0:
            n /= i
    i += 2
if n > 2:
    ans *= n
print(int(ans))
