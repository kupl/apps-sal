N = int(input())
R = list(map(int, input().split()))
X = [0]*8
p = 0
for r in R:
  if r >= 3200:
    p += 1
  else:
    X[r//400] = 1

s = sum(X)
if s == 0:
  print((str(1) + " " + str(p)))
else:
  print((str(s) + " " + str(s + p)))

