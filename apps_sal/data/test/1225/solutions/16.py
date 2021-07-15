def divi(n):
  if n > 1:
    return 2*divi(n//2) + 1
  else:
    return 1
h = int(input())
print(divi(h))
