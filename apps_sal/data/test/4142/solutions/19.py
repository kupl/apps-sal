s = input()

howmany = len(s)
judge = "Yes"

for x in range(howmany):
  if x % 2 == 0:
    if s[x] != "R" and s[x] != "U" and s[x] != "D":
      judge = "No"
      break
  else:
    if s[x] != "L" and s[x] != "U" and s[x] != "D":
      judge = "No"
      break
      
print(judge)
