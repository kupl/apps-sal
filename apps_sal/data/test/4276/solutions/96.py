n,T = map(int, input().split())
l = []
for i in range(n):
  c,t = map(int, input().split())
  if t <= T:
    l.append(c)
if l != []:
  print(min(l))
else:
  print("TLE")
