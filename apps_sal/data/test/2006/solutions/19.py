n,m=list(map(int,input().split()))
dst=set()
for _ in range(n):
  l=input()
  s=l.find('S')
  g=l.find('G')
  if s<g:
    print(-1)
    return
  else:
    dst.add(g-s)
print(len(dst))

