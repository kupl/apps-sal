a = list(map(str,input()))
b = list(map(str,input()))
c = list(map(str,input()))
s = a.pop(0)
while True:
  if a == [] and s == "a":
    print("A")
    return
  elif b == [] and s == "b":
    print("B")
    return
  elif c == [] and s == "c":
    print("C")
    return
  if s == "a":
    s = a.pop(0)
  elif s == "b":
    s = b.pop(0)
  elif s == "c":
    s = c.pop(0)

