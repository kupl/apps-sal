n=int(input())

v=list(map(int,input().split()))

lisa=[0 for _ in range(10**5)]
lisb=[0 for _ in range(10**5)]

for i in range(n):
  if i%2==0:
    lisa[v[i]-1]+=1
  else:
    lisb[v[i]-1]+=1

maxnuma=-1
maxnumb=-1

maxa=max(lisa)
maxb=max(lisb)


for i in range(10**5):
  if lisa[i]==maxa:
    maxnuma=i
for i in range(10**5):
  if lisb[i]==maxb:
    maxnumb=i


if maxnuma!=maxnumb:
  print((n-maxa-maxb))
else:
  lisa.sort(reverse=True)
  lisb.sort(reverse=True)
  print((n-max(lisa[0]+lisb[1],lisa[1]+lisb[0])))


