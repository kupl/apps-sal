n=int(input())
s=list(input())
from collections import deque
q=deque(s)
p=[]

while q:
  a=q.popleft()
  if a!="x":
    p.append(a)
    continue
  # ここではa==xをみたす
  try:
    f=p[-2]
    o=p[-1]
    if f=="f" and o=="o":
      p.pop()
      p.pop()
      continue
  except:
    pass
  p.append(a)
print(len(p))#,p)
