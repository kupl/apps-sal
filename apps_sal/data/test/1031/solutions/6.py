n = int(input())
a = list(map(int, input().split()))
x = [0] * (n + 1)
y = [0] * (n + 1)
for i in range(1, n + 1):
  x[i] = x[i - 1] + a[i - 1]
  y[i] = y[i - 1]
  if i % 2 == 0:
    y[i] -= a[i - 1]
  else:
    y[i] += a[i - 1]
# print(x)
# print(y)
m = min(y)
if m < 0:
  for i in range(n + 1):
    y[i] -= m
# print(y)
w = max(x)
h = max(y)
# print(h, w)
d = [[" "] * w for i in range(h)]
for i in range(n):
  if y[i] < y[i + 1]:
    for j in range(a[i]):
#       print(y[i] + j, x[i] + j, "/")
      d[y[i] + j][x[i] + j] = "/"
  else:
    for j in range(a[i]):
#       print(y[i] - j - 1, x[i] + j, "\\")
      d[y[i] - j - 1][x[i] + j] = "\\"
print("\n".join("".join(d[i]) for i in reversed(range(h))))
