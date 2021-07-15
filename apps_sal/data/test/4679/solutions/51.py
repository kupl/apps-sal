a = list(input())
b = list(input())
c = list(input())
next = a.pop(0)
while True:
  if next == "a":
    if a == []:
      print("A")
      break
    else:
      next = a.pop(0)
  elif next == "b":
    if b == []:
      print("B")
      break
    else:
      next = b.pop(0)
  else:
    if c == []:
      print("C")
      break
    else:
      next =c.pop(0)
