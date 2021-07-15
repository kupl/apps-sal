import math

n = int(input())

subs = 0

while(n > 0):
  if (n % 2 == 0):
    subs += n // 2
    n = 0
  else:
    sq = int(math.sqrt(n))
    found = False
    for i in range(2, sq + 1):
      if (n % i) == 0:
        found = True
        break

    if found:
      subs += 1
      n -= i
    else:
      subs += 1
      n = 0

print(subs)
