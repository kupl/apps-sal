s = input()
p = 0
m = 0

for i in s:
  if i == "+":
    p += 1
    m = max(m-1, 0)
  elif i == "-":
    m += 1
    p = max(p-1, 0)
print(p+m)

