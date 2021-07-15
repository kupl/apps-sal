A,B,K = map (int, input ().split ())
c = 0
if A < B:
  R = A
else:
  R = B
for i in range (R):
  I = R-i
  if A%I==0 and B%I==0:
    c += 1
    if c == K:
      print (I)
      break
