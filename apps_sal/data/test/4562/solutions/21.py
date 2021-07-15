n = int(input())
for i in range(100000):
  if n >= (10**5-i)**2:
    print((10**5-i)**2)
    return
