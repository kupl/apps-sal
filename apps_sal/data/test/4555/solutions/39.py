a,b,k = map(int, input().split())
setA = set(i for i in range(a,min(a+k,b+1)))
setB = set(j for j in range(b,max(b-k,a-1),-1))
l = list(setA|setB)
l.sort()
for m in l:
  print(m)
