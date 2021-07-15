n = int(input())
x = list(map(int, input().split()))

min_x = 100 * 100 * 100 + 1
for p in range(1, 100+1, 1):
  total = 0
  for xi in x:
    total += (xi - p) ** 2

  min_x = min([min_x, total])

print(min_x)


