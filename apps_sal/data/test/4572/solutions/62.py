S=input()
for i in "abcdefghijklmnopqrstuvwxyz":
  if not i in S:
    print(i)
    break
else:
  print("None")
