a = int(input())
b = int(input())
l = [1,2,3]
if a>b:
  l.pop(a-1)
  l.pop(b-1)
else:
  l.pop(b-1)
  l.pop(a-1)
print(l[0])
