A,B,N=map(int,input().split())
#if B==1:print(0);return
if N>=B:print((A*(B-1))//B)
else:
  print((A*N)//B-A*(N//B))
