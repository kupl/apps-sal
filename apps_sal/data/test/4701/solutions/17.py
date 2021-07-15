n = int(input())
k = int(input())
c = 1
for i in range(n):
  if c > k:
    c += k
  else:
    c *= 2
print(c)
