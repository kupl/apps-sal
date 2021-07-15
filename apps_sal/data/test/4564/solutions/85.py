S = input()
data = set()
for s in S:
  if s not in data:
    data.add(s)
  else:
    print("no")
    return
print("yes")
