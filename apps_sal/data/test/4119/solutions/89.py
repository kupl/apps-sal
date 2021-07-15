n,m=list(map(int,input().split()))
l=list(map(int,input().split()))

if n>=m:
  print((0))
else:
  num=n-1
  sl=sorted(l)

  dsl=[abs(sl[i+1]-sl[i]) for i in range(m-1)]

  dsl=sorted(dsl)
  print((sum(dsl[0:len(dsl)-num])))

