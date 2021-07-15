n = input()
from itertools import product
sum = 0
for i in range(len(n)-2):
  for j in list(product("753", repeat=i+3)):
    if int(''.join(j)) <= int(n) and len(set(j))==3:
      sum+=1
print(sum)
