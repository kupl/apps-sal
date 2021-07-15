n = int(input())
a, b = [list(map(int, input().split())) for i in range(2)]
s = 0
for v, c in zip(a, b):
  if v - c > 0:
    s += v - c
print(s)
