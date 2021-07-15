a,b,c,d = map(int,input().split())
if b < c:
  print(0)
  return
print(max(0, min(d,b)-max(a,c)))
