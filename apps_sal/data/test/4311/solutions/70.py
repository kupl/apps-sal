a = int(input())
l = [a]
for i in range(1000000):
  if a % 2 == 0:
    a = a//2
  else:
    a = a*3 + 1
  if l.count(a)==2:
    print((1+max([i for i, x in enumerate(l) if x == a])))
    break
  else:
    l.append(a)

