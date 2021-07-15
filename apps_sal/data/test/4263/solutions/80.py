s = input()
a, l = 0, 0
for i in s:
  if i in "ATGC":
    l += 1
  else:
    l = 0
  a = max(a, l)
print(a)
