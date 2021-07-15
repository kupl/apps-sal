x, k, d = map(int, input().split())

x = abs(x)
straight = min(k, x//d)
k -= straight
x -= straight*d

if k%2 == 0:
  print(x)
else:
  print(d-x)
