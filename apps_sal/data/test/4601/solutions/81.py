N,K = list(map(int,input().split()))
Hlist = list(map(int,input().split()))

Hlist = sorted(Hlist,reverse = True)
#print (Hlist)

if len(Hlist)>=K and K!=0:
  del Hlist[0:K]
elif len(Hlist)<K:
  del Hlist[0:len(Hlist)]

if len(Hlist)>0:
  print((sum(Hlist)))
else:
  print((len(Hlist)))

