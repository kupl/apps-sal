N = int (input ())
x = 0
for i in range (N):
  s,g = map (int, input ().split ())
  le = g-s+1
  x += le
print (x)
