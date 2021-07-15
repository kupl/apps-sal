import math
n = int(input())
inf = float("inf")
a = [inf]
b = [inf]
c = [inf]
ab = [inf]
ac = [inf]
bc = [inf]
abc = [inf]
for i in range(n):
  x,s = input().split()
  x = int(x)
  s_  = []
  for j in s:
    s_.append(j)
  s = sorted(s_)
  s = "".join(s)
  if s == "A":
    a.append(x)
  elif s == "B":
    b.append(x)
  elif s == "C":
    c.append(x)
  elif s == "AB":
    ab.append(x)
  elif s == "AC":
    ac.append(x)
  elif s == "BC":
    bc.append(x)
  elif s == "ABC":
    abc.append(x)
ans = float("inf")
a = min(a)
b = min(b)
c = min(c)
ab = min(ab)
ac = min(ac)
bc = min(bc)
abc = min(abc)
ans = min(a+b+c,a+bc,b+ac,c+ab,ab+ac,ab+bc,ac+bc,abc)
if ans == inf:
  print(-1)
else:
  print(ans)
