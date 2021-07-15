n = int(input())
for i in range(100000):
  if i**2 > n:
    print((i-1)**2)
    break
