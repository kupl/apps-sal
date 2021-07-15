s = input()
a = ""
b = 0
for i in s:
  if i in "ACGT":
    a += i
    if b < len(a):
      b = len(a)
  else:
    a = ""
print(b)
