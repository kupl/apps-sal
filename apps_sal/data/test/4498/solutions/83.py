a,b,c,d = [int(x) for x in input().split()]
res = "No"
if abs(c - a) <= d:
  res = "Yes"
if abs(a - b) <= d and abs(b - c) <= d:
  res = "Yes"
print(res)
