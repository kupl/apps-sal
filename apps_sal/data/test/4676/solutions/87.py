o = input()
e = input()
l = []
if len(o)-len(e) == 1:
  for i in range(len(e)):
    l.append(o[i])
    l.append(e[i])
  l.append(o[-1])
else:
  for i in range(len(o)):
    l.append(o[i])
    l.append(e[i])
print("".join(l))
