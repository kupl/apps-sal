input()
a = list(map(int, input().split()))
b = [0] + [0 for i in a]
c = [0] + [0 for i in a]
d = -1000
for i in range(len(a)):
  b[i + 1] = b[i] + a[i]
  c[i + 1] = c[i] + 1 - a[i]
for i in range(len(a)):
  for j in range(i + 1):
    d = max(d, c[i + 1] - c[j] - b[i + 1] + b[j])
print(d + b[-1])
