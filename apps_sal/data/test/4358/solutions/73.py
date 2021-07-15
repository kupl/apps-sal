N = int (input ())
l = []
a = 0
for i in range (N):
  x = int (input ())
  a += x
  l.append (x)
n = max (l)/2
print (round (a-n))
