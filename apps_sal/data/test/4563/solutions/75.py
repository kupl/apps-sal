import fractions
N=int(input())

vt=va=0
for _ in range(N):
  T,A=map(int,input().split())
  kt=-(-vt//T)
  ka=-(-va//A)
  if kt==0 and ka==0:
    vt=T
    va=A
  else:
    k=max(kt,ka)
    vt=k*T
    va=k*A
  
  #print(vt,va)
  
print(vt+va)
