N,M = map(int,input().split())
Hlist = list(map(int,input().split()))

anslist = [1]*N
for i in range(M):
  A,B = map(int,input().split())
  #print (Hlist[A-1])
  #print (Hlist[B-1])
  if Hlist[A-1]<Hlist[B-1]:
    anslist[A-1]=0
  elif Hlist[A-1]>Hlist[B-1]:
    anslist[B-1]=0
  elif Hlist[A-1]==Hlist[B-1]:
    anslist[A-1]=0
    anslist[B-1]=0
    
#print (anslist)
print (sum(anslist))
