a, b, k = map(int, input().split())
x = [i for i in range(a, min(a + k, b + 1))]
y = [i for i in range(max(a, b - k + 1), b + 1)]
for i in sorted(set(x + y)):
  print(i)
