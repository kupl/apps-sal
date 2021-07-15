def h(z):
  a = 0
  b = 1
  res = 1
  while True:
    a, b = b, a + b + 1
    if b >= z:
      break
    res += 1  
  return res
  
n = int(input())
print(h(n))  
