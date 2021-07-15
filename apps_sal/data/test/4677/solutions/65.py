s = input()
numB = 0
r = ""
for i in range(len(s))[::-1]:
  if s[i] == "B":
    numB = numB+1
    continue
  if numB > 0 and (s[i]=="0" or s[i]=="1"):
    numB = numB-1
    continue
  r = r + s[i]

print((''.join(list(reversed(r)))))


