N=int(input())

if N%2 or N<10:
  print(0)
else:
  cnt,n=0,1
  while n<=N:
    cnt+=N//(10*(n))
    n*=5
  print(cnt)
