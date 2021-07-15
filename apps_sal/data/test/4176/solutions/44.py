A, B = map(int, input().split())

def gcd(x, y):
  if x % y == 0:
    return y
  else:
    return gcd(y, x % y)

GCD = gcd(A, B)
a = A // GCD
b = B // GCD
print(a * b * GCD)
