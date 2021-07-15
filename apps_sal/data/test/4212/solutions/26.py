import itertools
n,m,q = map(int,input().split())
l = []
for i in range(q):
  tl = list(map(int,input().split()))
  l.append(tl)
#print(l)

lis = [i+1 for i in range(m)]
lis = list(itertools.combinations_with_replacement(lis, n))
#print(lis)
ans = 0
for i in lis:
  tmp = 0
  for j in range(q):
    a = l[j][1] - 1
    b = l[j][0] - 1
    if l[j][2] == i[a] - i[b]:
      tmp += l[j][3]
  ans = max(tmp,ans)
print(ans)
