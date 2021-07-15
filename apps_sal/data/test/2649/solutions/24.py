n=int(input())
l=[]
ar=[]
br=[]
for i in range(n):
  l.append(list(map(int,input().split())))
  ar.append(l[-1][0]+l[-1][1])
  br.append(l[-1][0]-l[-1][1])
ar.sort()
br.sort()
an=max(abs(ar[-1]-ar[0]),abs(br[-1]-br[0]))
print(an)
