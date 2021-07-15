r, D, x = map(int, input().split())

for i in range(10):
  if i == 0:
    weight = r*x - D
    print(weight)
  else:
    weight = r*weight - D
    print(weight)
