X = int(input())
X_ri = round(pow(X, 1/2))

while True:
  for i in range(2, X_ri + 1):
    if X % i == 0:
      break
  else:
    print(X)
    break
  X = X + 1
