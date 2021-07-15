n = int(input())
t = input()
t = str(t)
t = list(t)
t.append("#")
if t[0] == "0":
  for i in range(0,n,3):
    if t[i] != "0":
      if t[i] == "#":
        break
      else:
        print((0))
        return
    if t[i+1] != "1":
      if t[i+1] == "#":
        break
      else:
        print((0))
        return
    if t[i+2] != "1":
      if t[i+2] == "#":
        break
      else:
        print((0))
        return
if t[0] == "1" and t[1] == "1":
  for i in range(0,n,3):
    if t[i] != "1":
      if t[i] == "#":
        break
      else:
        print((0))
        return
    elif t[i+1] != "1":
      if t[i+1] == "#":
        break
      else:
        print((0))
        return
    if t[i+2] != "0":
      if t[i+2] == "#":
        break
      else:
        print((0))
        return
if t[0] == "1" and t[1] == "0":
  for i in range(0,n,3):
    if t[i] != "1":
      if t[i] == "#":
        break
      else:
        print((0))
        return
    if t[i+1] != "0":
      if t[i+1] == "#":
        break
      else:
        print((0))
        return
    if t[i+2] != "1":
      if t[i+2] == "#":
        break
      else:
        print((0))
        return
if n  == 1:
  if t[0] == "1":
    print((2*(10**10)))
    return
  else:
    print((10**10))
    return
if n ==2:
  if t[0] == "0" and t[1] == "1":
    print((10**10-1))
    return
  else:
    print((10**10))
    return
if n%3 == 0:
  if t[n-1] == "0" :
    p = n//3
    print((10**10-p+1))
  else:
    p = n//3
    print((10**10-p))
elif n%3 == 2:
  if t[0] == "0" and t[n-1] =="1":
    p = ((n-2)//3)+2
    print((10**10-p+1))
  else:
    p = n//3
    print((10**10-p))
else:
  p = n//3
  print((10**10-p))



