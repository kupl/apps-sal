n, k = [int(input()) for _ in range(2)]

result = 10 ** 9

for bit in range(2 ** n):
  
  tmp = 1
  for i in range(n):
    if bit & (1 << i):
      tmp *= 2
    else:
      tmp += k
  
  result = min(result, tmp)
  
print(result)
