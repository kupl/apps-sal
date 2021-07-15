s = input()

res = 0
c = 0
for i in range(len(s)):
  if s[i] == "A" or s[i] == "G" or s[i] == "C" or s[i] == "T":
    c += 1
  else:
    res = max(res,c)
    c = 0
res = max(res,c)
print(res)
