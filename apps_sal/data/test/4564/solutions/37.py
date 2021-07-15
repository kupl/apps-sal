u = input()
for i in range(len(u)):
  for j in range(i+1,len(u)):
    if u[i]==u[j]:
      print("no")
      return
print("yes")
