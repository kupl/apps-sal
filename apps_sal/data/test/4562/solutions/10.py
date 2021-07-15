n = int(input())

for i in range(n, 0, -1):
  j = int(i ** 0.5)
  if int(j) ** 2 == i:
    break
print(i)

