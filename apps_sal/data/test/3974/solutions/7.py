inp=input()
inclb=0
outclb=0
seen=0
i=0
for i in range(0,len(inp)):
 if inp[i] == "-":
  outclb += 1
  if inclb > 0:
   inclb -= 1
  else:
   seen += 1
 else:
  inclb += 1
  if outclb > 0:
   outclb -= 1
  else:
   seen += 1
print(seen)
