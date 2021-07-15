h,w = map(int,input().split())
a = []
hh = 0
for _ in range(h):
  x = [xx for xx in input()]
  if x.count("#") > 0:
    a.append(x)
    hh += 1
b = []

count = 0
if hh > 1:
  wlist = []
  for i in range(w):
    for j in range(hh):
      b.append(a[j][i])
    if b.count("#") == 0:
      wlist.append(i)
    b = []
  for k in wlist:
    for l in range(hh):
      a[l].pop(k-count)
    count += 1
  for m in range(len(a)):
    print("".join(a[m]))
else:
  a = list(*a)
  ans = [aa for aa in a if aa == "#"]
  print("".join(ans))
