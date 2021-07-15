n,m,s = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

low = 0
high = 0
for i in range(m):
  if a[i] < s:
    low += 1
  else:
    high += 1
print(min(low,high))
