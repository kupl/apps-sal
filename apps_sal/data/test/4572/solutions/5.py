S = input()
l = sorted(list(set(S)))

ans = ""
for i in range(len(l)):
  if ord(l[i]) !=  97 + i:
    ans = chr(97+i)
    break
  elif i == 25 and l[i] == "z":
    ans = "None"

if ans != "":
 print(ans)
else:
  print(chr(ord(l[-1])+1))
