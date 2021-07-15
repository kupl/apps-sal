s = input()
patern = "heidi"
prev = 0
for c in patern:
  ok = False
  for i in range(prev, len(s)):
    prev += 1
    if s[i] == c:
      ok = True
      break
  if not ok:
    print ("NO\n")
    return
print ("YES\n")
