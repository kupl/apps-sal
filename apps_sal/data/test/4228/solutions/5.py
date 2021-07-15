N,L=map(int,input().split())
sum_apple=0
if L<0 and L+N-1<0:
  for i in range(1,N):
    sum_apple+=L+i-1
elif L>0 and L+N-1>0:
  for i in range(2,N+1):
    sum_apple+=L+i-1
else:
  for i in range(1,N+1):
    sum_apple+=L+i-1
print(sum_apple)
