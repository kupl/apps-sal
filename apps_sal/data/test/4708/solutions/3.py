n = int(input())
k = int(input())
x = int(input())
y = int(input())

if n > k :
  print(k*x + (n-k)*y)
elif n <= k:
  print(n*x)
