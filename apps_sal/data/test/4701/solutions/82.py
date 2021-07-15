N = int (input ())
K = int (input ())
s = 1
for i in range (N):
  if s < K:
    s = s*2
  else:
    s += K
print (s)
