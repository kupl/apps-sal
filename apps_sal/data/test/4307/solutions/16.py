n = int(input())
t = 0
for i in range(1, n+1):
  if i % 2 == 1:
    s = 1
    for j in range(1, i//2 + 1):
      if i % j == 0:
        s += 1
    if s == 8:
      t += 1
print(t)
