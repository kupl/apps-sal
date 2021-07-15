n = int(input())
count = 0
x = {}

for i in range(n):
  s = "".join(sorted(input()))
  if s in x:
    count += x[s]
    x[s] += 1
  else:
    x[s] = 1
print(count)
