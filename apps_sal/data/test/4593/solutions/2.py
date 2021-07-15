from math import *

x = int(input())

lst1 = list(range(2, int(sqrt(1000)) + 1))
lst2 = [1, 1000]

for n in lst1:
   i = 2
   while n ** i < 1000:
      lst2.append(n ** i)
      i += 1

lst2 = list(set(lst2))
lst2.sort()

for i in range(len(lst2)):
   if x < lst2[i]:
      print(lst2[i - 1])
      return

print(lst2[-1])
