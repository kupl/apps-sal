N = int(input())
K = int(input())
X = int(input())
Y = int(input())
price = 0
if N <= K:
  for i in range(N):
    price += X
  print(price)
else:
  for i in range(K):
    price += X
  for i in range(N-K):
    price += Y
  print(price)
