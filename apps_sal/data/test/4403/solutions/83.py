li = list(map(str, input()))
S=0
for i in range(4):
  if li[i]=="+":
    S=S+1
  else:
    S=S-1
print(S)
