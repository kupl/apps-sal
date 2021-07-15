N = int(input())
result = 0
num = 1
for i in range(7):
  if N >= num:
    result = num
  else:
    None
  num *= 2
print(result)
