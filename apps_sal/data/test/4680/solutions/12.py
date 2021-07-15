l = [int(x) for x in input().split()]
l = sorted(l)
if l.count(5)==2 and l.count(7)==1:
  print("YES")
else:
  print("NO")
