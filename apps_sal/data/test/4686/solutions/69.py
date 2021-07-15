w = input()
wl = []

for i in range(len(w)):
  wl.append(w[i])
  
wl.sort()

a = 1
judge = 1
if len(w)%2 == 0:
  for n in range(len(w)-1):
    if wl[a+n] == wl[a+n-1]:
      judge += 1
    else:
      if judge%2 != 0:
        print("No")
        return
      else:
        judge = 1
    if n == len(w)-2:
      if judge%2 == 0:
        print("Yes")
      else:
        print("No")
else:
  print("No")
