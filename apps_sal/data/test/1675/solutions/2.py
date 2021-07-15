n = int(input())
a = []
b = [0] * 100001
for i in range(n):
  x, y = map(int, input().split())
  a += [y]
  b[x] += 1
print("\n".join("{} {}".format(n - 1 + b[y], n - 1 - b[y]) for y in a))
