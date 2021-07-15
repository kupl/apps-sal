n = int(input())
s = list(input())
ans = 0
c = 0
fh = []
lh = s
for i in range(n):
  tmp = lh.pop(0)
  if tmp not in fh:
    if tmp in lh:
      c += 1
  elif tmp not in lh:
    c -= 1
  fh.append(tmp)
  ans = max(ans, c)
print(ans)
