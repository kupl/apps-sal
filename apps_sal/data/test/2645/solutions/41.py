import math
s = input()
 
ans = 0
 
r = 0
p = 0
c = 0
for j in s:
  c = r-p
  if j == 'g':
    if c > 0:
      p += 1
      ans += 1
    else:
      r += 1
  else:
    if c > 0:
      p += 1
    else:
      r += 1
      ans -= 1
print (ans)
