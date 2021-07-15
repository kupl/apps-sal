n = int(input())
s = list(map(str,input()))
ansl = []
for i in range(1,n):
  ans = 0
  x = list(set(s[:i]))
  y = list(set(s[i:]))
  for j in range(len(x)):
    if x[j] in y:
      ans += 1
  ansl.append(ans)
print(max(ansl))
