n = int(input())
a = [0] * 5
for i in range(n):
  s = input()
  if s[0] == "M":
    a[0] += 1
  elif s[0] == "A":
    a[1] += 1
  elif s[0] == "R":
    a[2] += 1
  elif s[0] == "C":
    a[3] += 1
  elif s[0] == "H":
    a[4] += 1

res = 0
res += a[0] * a[1] * a[2]
res += a[0] * a[1] * a[3]
res += a[0] * a[1] * a[4]
res += a[0] * a[2] * a[3]
res += a[0] * a[2] * a[4]
res += a[0] * a[3] * a[4]
res += a[1] * a[2] * a[3]
res += a[1] * a[2] * a[4]
res += a[1] * a[3] * a[4]
res += a[2] * a[3] * a[4]
print(res)
