from collections import Counter as c
N,K,Q,*A = map(int,open(0).read().split())

C = c(A)
#print(C)
for i in range(1,N+1):

  print("Yes" if K-Q+C.get(i,0)>0 else "No")
