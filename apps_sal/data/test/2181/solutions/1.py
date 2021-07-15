from math import floor
a, d = map(float, input().split())
n = int(input())

res = []
for i in range(n):
  rec = i*d + d
  tra = floor(rec/a) % 4
  seg = rec - floor(rec/a)*a
  # print("D>",rec, tra, seg)
  if tra == 0:
    res.append("%.8f %.8f" % (seg, 0.0))
  elif tra == 1:
    res.append("%.8f %.8f" % (a, seg))
  elif tra == 2:
    res.append("%.8f %.8f" % (a-seg, a))
  elif tra == 3:
    res.append("%.8f %.8f" % (0.0, a-seg))
    
print("\n".join(res))
