s = str(input())
strFindA = ''
strFindZ = ''

for i in range(len(s)):
  if s[i] == "A":
    strFindA = s[i:]
    break

for i in reversed(range(len(strFindA))):
  if strFindA[i] == "Z":
    strFindZ = strFindA[:i+1]
    break

print(len(strFindZ))
