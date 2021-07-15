n = int(input())
a = list(input())
wcnt,ecnt,ans,box = 0,0,0,[]
W = a.count("W")
E = a.count("E")
for i in range(n-1):
  if a[i] == "W":
    box.append(E+wcnt)
    wcnt += 1
    W -= 1
  else:
    box.append(E+wcnt)
    ecnt += 1
    E -= 1
if a[n-1] == "W":
  W -= 1
  box.append(E+wcnt)
  wcnt += 1
else:
  E -= 1
  box.append(E+wcnt)
  ecnt += 1
print(min(box))
