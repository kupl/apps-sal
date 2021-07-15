s = int(input())
a = [s]
while True:
  if a.count(a[-1]) == 2:
    print(len(a))
    return
  if a[-1]%2 == 0:
    a.append(a[-1]/2)
  else:
    a.append(3*a[-1]+1)
