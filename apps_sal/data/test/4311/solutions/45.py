s = int (input ())
l = []
a = 0
l.append (s)
for i in range (1000000):
  a += 1
  if s%2 == 0:
    s = round(s/2)
  else:
    s = s*3+1
  if l.count (s) != 0:
    print (a+1)
    break
  else:
    l.append (s)
