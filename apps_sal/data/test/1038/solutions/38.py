A,B = map(int,input().split())

def f(x):
  res = 0
  while x % 4 != 3:
    res ^= x
    x -= 1
  return res

print(f(A-1)^f(B))
