N, M, X, Y = list([int(a) for a in input().split(" ")])
x = list([int(b) for b in input().split(" ")])
y = list([int(c) for c in input().split(" ")])
x.append(X)
y.append(Y)
x.sort()
y.sort()
if x[-1] < y[0]:
  print("No War")
else:
  print("War")

