n,m = map(int, input().split())
l = [[] for _ in range(n)]
ac,wa = (0,0)
for i in range(m):
  p,s = input().split()
  p = int(p)
  if s == "AC":
    if s not in l[p-1]:
      l[p-1].append(s)
      ac += 1
      wa += l[p-1].count("WA")
  else:
    l[p-1].append(s)
print(ac,wa)
