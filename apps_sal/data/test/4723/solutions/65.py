s = input()
t = input()

n = len(s)
m = len(t)

for i in range(n-m, -1, -1):
  x = s[i:i+m]
  for j in range(m+1):
    if j == m:
      print(((s[:i]+t+s[i+m:]).replace("?","a")))
      return
    if x[j] == "?": continue
    elif x[j] != t[j]: break
    
print("UNRESTORABLE")

