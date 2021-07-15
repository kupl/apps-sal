n = int(input())
t = input()
if n == 1:
  if t == "1":
    print((2*10**10))
  else:
    print((10**10))
elif n == 2:
  if t == "11" or t == "10":
    print((10**10))
  elif t == "01":
    print((10**10-1))
  else:
    print((0))
else:
  if t[:3] == "110":
    a = 0
  elif t[:3] == "101":
    a = 1
  elif t[:3] == "011":
    a = 2
  else:
    print((0))
    return
  b = a
  for i in t[3:]:
    if i != "110"[b%3]:
      print((0))
      return
    b += 1
  print((10**10-(a+n-1)//3))

