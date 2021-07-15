s = input()
d = len(s)
n = int((d-1)/2)
for i in range(n):
  x = int((d-3)/2 -i)
  if s[i] == s[d-i-1] ==s[x]:
    continue
  else:
    print('No')
    return
print('Yes')
