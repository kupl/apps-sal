n,m = list(map(int,input().split()))
if n >= m :
  print((0))
else:
  ls=[int(s) for s in input().split()]
  ls.sort()
  d=[ls[i+1]-ls[i] for i in range(m-1)]
  d.sort()
  print((sum(d[:m-n])))

