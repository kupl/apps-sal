a=input().split(' ')
A=int(a[0])
B=int(a[1])
K=int(a[2])
if B-A+1<=K*2:
  for i in range(A,B+1):
    print(i)
else:
  for i in range(K):
    print((A+i))
  for i in range(K):
    print((B-K+1+i))

