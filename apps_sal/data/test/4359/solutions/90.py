import math
s = 0
m = 10
for i in range(5):
  n = int(input())
  if n % 10 != 0:
    m = min(m, int(str(n)[-1]))
    
  s += math.ceil( n * 0.1 )
if m % 10 != 0:
  s +=  m * 0.1 - 1
print((int(s*10)))

